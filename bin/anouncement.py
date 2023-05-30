#!/usr/bin/python3

# Requires python 3.10+ for match syntax
#
# Reference: https://community.atlassian.com/t5/Jira-Software-questions/Is-there-a-way-to-use-the-JIRA-API-to-retrieve-Release-Notes-of/qaq-p/1678046

import subprocess, os, sys, requests, json

def printUsage():
    print("python3 anouncement.py [-post] [-security] [-stable] [-maintenance] username password version")

def releaseName(release):
    return release['name']
    
def getSeriesReleasesFromNamePart(versionNumber):
    response = requests.get(jiraBaseUrl + 'rest/api/2/project/' + project + '/versions', auth=auth)
    versions = response.json()

    release = None
    
    for version in versions:
        if (versionNumber in version['name']):
            release = version
            break
    
    if not release:
       raise ValueError('Version number ' + versionNumber + ' not found')
    
    series = release['name'][0:4]
    releaseVersions = []
    for version in versions:
        if ((version['name'][0:4] == series) and (version['name'] <= release['name'])):
            releaseVersions.append(version)
    
    releaseVersions.sort(key=releaseName,reverse=True)
    
    # for version in releaseVersions:
    #   print( version['name'] + ': '+json.dumps(version))
       
    return releaseVersions

def getProjectIssuesFromVersion(projectVersion):
    jql = 'project = ' + project + ' AND fixVersion = "' + projectVersion['name'] + '" AND resolution IS NOT EMPTY ORDER BY key'
    params = {'projectId':projectVersion['projectId'], 'maxResults':1000, 'jql':jql}
    response = requests.get(jiraBaseUrl + '/rest/api/2/search', auth=auth, params=params)
    return response.json()

def gitUser():
    output = subprocess.check_output('git config --global user.name', shell=True)
    return output.decode('utf-8').strip()

def mdHeader(releaseVersion,series,author,secuirty):


   name = releaseVersion['name']
   print(json.dumps(releaseVersion))
   print('')
   print('---')
   print('author: '+author)
   print('layout: post')
   print('title: GeoServer '+name+' Released')
   print('categories:')
   print(' - Announcements')
   print('tags:')
   
   print(series)
   
   match series:
      case 'release candidate':
         print('- Release Candidate')
      case 'milestone':
         print('- Milestone Release')
      case _:
         print('- Release')
   
   if secuirty:
      print('- Vulnerability')
      
   print('release: release_'+name[0:1]+''+name[2:4])
   print('version: '+name)
   print('jira_version: '+releaseVersion['id'])
   print('---')
      
def mdAnouncement(releaseVersion,series,author):
    name = releaseVersion['name']
    
    print('GeoServer ['+name+'](https://geoserver.org/release/'+name+'/) release is now available')
    print('with downloads (')
    print('[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/'+name+'/geoserver-'+name+'-bin.zip/download),')
    print('[war](https://sourceforge.net/projects/geoserver/files/GeoServer/'+name+'/geoserver-'+name+'-war.zip/download),')
    print('[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/'+name+'/GeoServer-'+name+'-winsetup.exe/download))')
    print(', along with ')
    print('[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/'+name+'/geoserver-'+name+'-htmldoc.zip/download) and')
    print('[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/'+name+'/extensions/).')
    print('')
    
    if series == "release candidate":
       print('This is a release candidate intended for public review and feedback,')
    elif series == "milestone":
       print('This is a milestone release providing a preview of upcoming functionality for testing and feedback. This release is')
    elif series == "maintenance":
       print('This is a maintenance release of GeoServer provided as an update for production systems. This release is')
    else:
       print('This is a stable release of GeoServer recommended for production use,')
       
    print('made in conjunction with GeoTools XX.X, and GeoWebCache 1.XX.X.')
    print('')
    print('Thanks to '+author+' for making this release.')
    print('')

def mdSecurityConsiderations():
    print("## Security Considerations")
    print('')
    print('This release addresses a security vulnerabilities and is considered an essential upgrade for production systems.')
    print('')
    print('* [CVE-2023-XXXXX Advisory](https://github.com/geoserver/geoserver/security/advisories/GHSA-XXXX-xxxx-xxxx)')
    print('* [GEOS-XXXX Summary](https://osgeo-org.atlassian.net/browse/GEOS-XXXXX')
    print('')
    
def mdLinkReleaseNotes(versionNumber):
    return '[' + versionNumber +  '](https://github.com/geoserver/geoserver/releases/tag/'+versionNumber+')'

def mdIssue(issue):
    print('* [' +  issue['key'] + '](' + jiraBaseUrl + '/browse/' + issue['key'] + ') ' + issue['fields']['summary'])

def collectIssueTypeNames(issues):
    issueTypeNames = []
    for issue in issues:
        typeName = issue['fields']['issuetype']['name']
        if typeName not in issueTypeNames:
            issueTypeNames.append(typeName)
    
    orderedTypeNames = ['New Feature','Improvement','Bug','Task','Sub-task']
    for typeName in orderedTypeNames:
        if typeName not in issueTypeNames:
           orderedTypeNames.remove(typeName)

    for typeName in issueTypeNames:
        if typeName not in orderedTypeNames:
           orderedTypeNames.append(typeName)
    
    return orderedTypeNames

def mdReleaseNotes(releaseVersion, projectIssues, releaseVersions):
        
    print('## Release notes')
    
    issueTypeNames = collectIssueTypeNames(projectIssues['issues'])
    for issueTypeName in issueTypeNames:
        print('')
        print(issueTypeName + ':')
        print('')
        for issue in projectIssues['issues']:
            if issue['fields']['issuetype']['name'] == issueTypeName:
                mdIssue(issue)
    print('')
    print('For the complete list see [' + mdLinkReleaseNotes( releaseVersion['name']) +' release notes.')

    print('')
    
def mdSeries(releaseVersion, releaseVersions):
    print('# About GeoServer ' + releaseVersion['name'][0:4] + ' Series')
    print('')
    print('Additional information on GeoServer ' + releaseVersion['name'][0:4] + " series:")
    print('')
    print('* ')
    print('')
    print('Release notes:')
    print('( ' + mdLinkReleaseNotes(releaseVersion['name']) )
    for version in releaseVersions[1:]:
        print('| ' + mdLinkReleaseNotes(version['name']) )
    print(')')

project = 'GEOS'
jiraBaseUrl = 'https://osgeo-org.atlassian.net/'
post = False
security = False
stable = False
maintenance = False
argv = []

for arg in sys.argv:
   if arg[0:1] == '-':
      if arg == "-post":
          post = True
      elif arg == "-security":
          security = True
      elif arg == "-stable":
          stable = True
      elif arg == "-maintenance":
          maintenance = True 
      else:
          printUsage()
          exit()
   else:
      argv.append(arg)

if len(argv) != 4:
   printUsage()
   exit()

# auth=(user, password)
auth=(argv[1], argv[2])
name = argv[3]

if stable:
   series = 'stable'
elif maintenance:
   series = 'maintenance'
elif "RC" in name:
   series = "release candidate"
elif "M" in name:
   series = "milestone"
elif name[5:] < '3':
   series = 'stable'
else:
   series = 'maintenance'

author = gitUser()

releaseVersions = getSeriesReleasesFromNamePart(name)
releaseVersion = releaseVersions[0]
# print(json.dumps(projectVersion, indent=2))

projectIssues = getProjectIssuesFromVersion(releaseVersion)
# print(json.dumps(projectIssues, indent=2))

if post:
   if not releaseVersion['released']:
     print('Release '+name+' not released yet in Jira')
     print(json.dumps(releaseVersion))
     exit()
     
   elif 'releaseDate' not in releaseVersion or not releaseVersion['releaseDate']:
     print('Release '+name+' releaseDate not defined in Jira')
     print(json.dumps(releaseVersion))
     exit()
  
   filename = '../_posts/'+releaseVersion['releaseDate']+'-geoserver-'+name.replace('.','-')+'-released.md'
      
   if os.path.exists(filename):
      print('File already exists: '+filename)
      exit()
   
   print('Generating post to '+filename)
   print('This is an outline only, some editing will be required!')
   
   stdout_fileno = sys.stdout
   sys.stdout = open(filename, 'w')

mdHeader(releaseVersion,series,author,security)
mdAnouncement(releaseVersion,series,author)
if security:
  mdSecurityConsiderations()

mdReleaseNotes(releaseVersion, projectIssues, releaseVersions)
mdSeries(releaseVersion,releaseVersions)

if post:
   sys.stdout.close()
   sys.stdout = stdout_fileno