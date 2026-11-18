---
author: Andrea Aime
date: 2026-11-18
layout: post
title: "Java4Shell (CVE-2026-114938): add one Java flag to GeoServer today"
categories:
- Vulnerability
---

A critical vulnerability in the Java runtime became public on 17 November 2026. It goes by the name Java4Shell ([CVE-2026-114938](https://www.cve.org/CVERecord?id=CVE-2026-114938)), and it is a memory corruption bug in the accelerated Base64 decoder of the Java virtual machine.

The bug is in Java, not in GeoServer, but every server application that runs on an affected Java inherits it. The good news is that the fix is easy, safe and quick: one Java flag switches off the affected code.

```
-XX:-UseBASE64Intrinsics
```

Add the flag to the Java options and restart GeoServer, nothing else is needed. It works with every GeoServer version, and GeoServer, its configuration and its data directory stay as they are. If you run a GeoServer, please do it today.

Public reports name Java 17.0.6 and newer, Java 21 and Java 25, on x86-64 processors with the AVX-512 VBMI instruction set, and Oracle also lists a Java 8 build, `8u511b33-perf`. These reports are one day old and the list keeps changing. At the time of writing they mention no attacks in the wild, so there is time to act calmly, and no reason to wait. Even if your Java version, processor or architecture might not be affected, we recommend applying the flag anyway: it is safe everywhere, and it covers you if a later report extends the list.

## Adding the flag

The flag is a Java startup option, so it goes wherever the installation sets its Java options. One way works for any setup: the `JAVA_TOOL_OPTIONS` environment variable, which Java reads at startup (if the variable already has a value, append the flag to it). Restart GeoServer after the change.

A few examples:

* **Binary package**: run `export JAVA_OPTS="$JAVA_OPTS -XX:-UseBASE64Intrinsics"` before `bin/startup.sh`.
* **Tomcat**: add `CATALINA_OPTS="$CATALINA_OPTS -XX:-UseBASE64Intrinsics"` to `bin/setenv.sh`.
* **Official GeoServer Docker image** (`docker.osgeo.org/geoserver`): add `-e JAVA_TOOL_OPTIONS=-XX:-UseBASE64Intrinsics` to `docker run`.

Some Java 8 builds do not know the flag and stop at startup with the message `Unrecognized VM option 'UseBASE64Intrinsics'`. Such a build does not include the accelerated decoder, so this vulnerability cannot be used against it. In that case remove the flag and start GeoServer again.

## Checking that the flag is active

The check depends on what GeoServer runs on: a full JDK, or a JRE.

### With a JDK

The JDK includes `jinfo`, a tool that asks the running JVM for the value of the flag. On Linux and macOS, for the binary package:

```
jinfo -flag UseBASE64Intrinsics $(pgrep -f 'start\.jar' | head -1)
```

For Tomcat:

```
jinfo -flag UseBASE64Intrinsics $(pgrep -f 'org\.apache\.catalina\.startup\.Bootstrap' | head -1)
```

On Windows, run `jps -l` to find the process id of GeoServer, then pass it to `jinfo`:

```
jinfo -flag UseBASE64Intrinsics PID
```

Run the commands as the operating system user that runs GeoServer, for example with `sudo -u tomcat` in front when Tomcat runs as the `tomcat` user. `jinfo` prints one line:

* `-XX:-UseBASE64Intrinsics` (minus sign): the flag is active.
* `-XX:+UseBASE64Intrinsics` (plus sign): the flag is missing and the JVM might be vulnerable. Check the startup options, restart, then run the command again.

### With a JRE

A JRE has no `jinfo`, so the check looks at how the Java process was started. On Linux, replace `PID` with the process id of GeoServer:

```
cat /proc/PID/cmdline /proc/PID/environ | tr '\0' '\n' | grep -o '[^ ]*UseBASE64Intrinsics'
```

A line with `-XX:-UseBASE64Intrinsics` means the flag is there. No output means the flag is missing.

On Windows, PowerShell lists the command line of the Java processes:

```
Get-CimInstance Win32_Process -Filter "Name = 'java.exe'" | Select-Object ProcessId, CommandLine
```

The command line shows the flag when it comes from the Java options. When it comes from `JAVA_TOOL_OPTIONS`, look at the console output instead: on every operating system, Java starts it with the line `Picked up JAVA_TOOL_OPTIONS: -XX:-UseBASE64Intrinsics`.

## After the flag

The flag only tells Java to use its standard Base64 decoder in place of the accelerated one, so GeoServer works as before and we expect no visible change in performance. It is a mitigation though, and the permanent fix is a Java update.

At the time of writing, several widely used OpenJDK distributions, such as Eclipse Temurin and the packages of the main Linux distributions, do not have a patched build yet. Update Java as soon as the vendor of your distribution has one (the vendor advisory gives the exact version number). After the update the flag can stay in place, or be removed.

If something is unclear, ask on the [user forum](https://discourse.osgeo.org/c/geoserver/user/51). Security issues go through the [GeoServer security policy](https://github.com/geoserver/geoserver/security/policy), as usual.
