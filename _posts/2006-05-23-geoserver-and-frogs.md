---
author: Jody Garnett
date: 2006-05-23
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/05/23/GeoServer+and+FROGs
wayback: https://web.archive.org/web/20061007120017/http://docs.codehaus.org:80/display/GEOS/2006/05/23/GeoServer+and+FROGs
title: "GeoServer and FROGs"
categories:
- Announcements
---

Chat was held on skype do to firewall issues, next meeting w/ demos in two weeks time.\
\[6:02:22 PM\] Jody Garn... says: morning!\
\[6:02:31 PM\] Jody Garn... says: so it is meeting time\
\[6:02:35 PM\] Jody Garn... says: we got lots of people hanging around\
\[6:02:40 PM\] Jody Garn... says: how should we start?\
\[6:03:27 PM\] Peter Schut says: I'm still on a telecon, so will be typing slowly...\
\[6:03:32 PM\] \* Jody Garnett added Andrea Aime, Chris Holmes, Gerhard Goosen, Justin Deoliveira, Clint Lewis, Oliver Loe, Xiaoyuan Geng, simboss18830 to this chat\
\[6:03:37 PM\] Jody Garn... says: no worries\
\[6:03:52 PM\] Jody Garn... says: um telecon w/ some other people?\
\[6:04:02 PM\] Peter Schut says: Yep. Multitasking\
\[6:04:08 PM\] Jody Garn... says: fun!\
\[6:04:12 PM\] Peter Schut says: It should end really soon.\
\[6:04:29 PM\] Jody Garn... says: got quite a turn out ... imagine we should post logs to geoserver site.\
\[6:04:45 PM\] Jody Garn... says: (for those showin gup now Peter is on the phone)\
\[6:04:49 PM\] Clint Lewis says: Quite a turn out indeed\
\[6:05:06 PM\] Jody Garn... says: Peter we talked a bit about frogs during todays meeting, all comments about your logo were in fun :)\
\[6:05:09 PM\] \* Andrea Aime has changed the chat topic to "Frogs/Geoserver collaboration"\
\[6:05:23 PM\] Andrea Ai... says: Yeah, each time I look at it I see a dog\
\[6:05:26 PM\] Peter Schut says: I like it! It's Roberto's doing...\
\[6:05:29 PM\] Jody Garn... says: The main feedback was one of focus :)\
\[6:05:44 PM\] Andrea Ai... says: Takes me a few seconds concentration to actually see the frog... :P\
\[6:05:46 PM\] Jody Garn... says: so Justin is probably going to give us an agenda in a bit (or chris)\
\[6:05:56 PM\] Jody Garn... says: but for now we can kinda of chat until order is called ...\
\[6:06:48 PM\] Justin Deo... says: ummm... ok i thought that was going to be you\
\[6:06:58 PM\] Jody Garn... says: I can bang out an agenda ...\
\[6:07:04 PM\] Jody Garn... says: what do we want to cover?\
\[6:07:05 PM\] Justin Deo... says: i would say andreas evaluation of frogs should be on there\
\[6:07:14 PM\] Justin Deo... says: i can talk a bit about what I would like to see in geoserver\
\[6:07:20 PM\] Jody Garn... says: 0) cholmes gives us an introduction and hint for direction\
\[6:07:35 PM\] Jody Garn... says: 1) jdeolive (probably did not write your article) chats about geoserver direction\
\[6:07:41 PM\] Justin Deo... says: nope, sorry\
\[6:07:45 PM\] Jody Garn... says: 2) peter talks about frogs hopping forward\
\[6:08:18 PM\] Jody Garn... says: basically lets meet each other, see where we want to go, my main interest\
\[6:08:26 PM\] Xiaoyuan ... says: Roberto is coming\
\[6:08:42 PM\] Chris Holm... says: I guess 0) is me then...\
\[6:08:53 PM\] Jody Garn... says: is that of cooperation. I am amazed that there are two efforts interested in an obscure spec like the OWS stack, and would like to see things move.\
\[6:09:03 PM\] Jody Garn... says: any one else got an agenda item?\
\[6:09:34 PM\] Jody Garn... says: 3) Open discussion\
\[6:09:43 PM\] Jody Garn... says: over to you chris :)\
\[6:09:51 PM\] Chris Holm... says: Basically the root thought is: hey, we're both working on frameworks for open geospatial services, and they're both in Java, so it's at least worth seeing if we might be able to work together.\
\[6:10:08 PM\] Chris Holm... says: We seem to both have the desire to, wanting a collaborative approach...\
\[6:10:17 PM\] Chris Holm... says: with plug-in architectures to enable more collaboration.\
\[6:10:25 PM\] Chris Holm... says: So we're meeting to figure out if the tech can work together.\
\[6:10:41 PM\] Chris Holm... says: FROGS actually has a working plug-in architecture of sorts, geoserver is working on evolving towards one.\
\[6:11:08 PM\] Chris Holm... says: And since a key step in that evolution is taking place now, we can try to figure out what to do to make things work right down the road.\
\[6:11:40 PM\] Chris Holm... says: So I'm psyched that this meeting is happening...\
\[6:11:46 PM\] Chris Holm... says: over to you justin.\
\[6:11:54 PM\] Jody Garn... says: +1\
\[6:12:00 PM\] Justin Deo... says: thanks chris\
\[6:12:19 PM\] Justin Deo... says: so basically what i have been working on is getting geoserver to this place while keeping the app relativley stable\
\[6:12:27 PM\] Justin Deo... says: here are my goals for hte project\
\[6:12:35 PM\] Justin Deo... says: 1. Plug-in system\
\[6:12:37 PM\] Justin Deo... says: 2. Easy to develop\
\[6:12:45 PM\] Xiaoyuan ... says: Have our geoserver folks had high level document already? If so we can start from there\
\[6:12:48 PM\] Justin Deo... says: 3. Integreation (like slotting into J2EE)\
\[6:13:06 PM\] Justin Deo... says: we have architecture docs yes\
\[6:13:17 PM\] Justin Deo... says: nothing relating to the stuff we have been working on this week though\
\[6:13:26 PM\] Jody Garn... says: (what we have is email discussion on several lists, a few articles, and way too much experience :) )\
\[6:13:31 PM\] Justin Deo... says: jody can forward you to the approrpiate documetnation\
\[6:13:45 PM\] Justin Deo... says: so the route we have decided to take\
\[6:13:51 PM\] Justin Deo... says: is using spring as our base\
\[6:13:58 PM\] Justin Deo... says: it gets us a lot of what we ant\
\[6:14:00 PM\] Justin Deo... says: want\
\[6:14:06 PM\] Jody Garn... says: vwfs.refractions.net for background, when we migrated from geoserver servlets/singletons to modules in the application context.\
\[6:14:15 PM\] Justin Deo... says: ease of developement, integration for everything, etc...\
\[6:14:26 PM\] Justin Deo... says: however its not a full blown plug-in system\
\[6:14:37 PM\] Justin Deo... says: its just a nice way to "wire" modules together\
\[6:14:54 PM\] Jody Garn... says: depends on definition, we are a bit spoiled after working with the Eclipse plugin system for uDig.\
\[6:14:56 PM\] Justin Deo... says: so there is no magic going on at runtime (dynamic loading / unloading of plugins, etfc...)\
\[6:15:14 PM\] Justin Deo... says: and so that is about it\
\[6:16:09 PM\] \* Andrea Aime added Roberto Caron to this chat\
\[6:16:25 PM\] Justin Deo... says: why dont we turn things over to Andrea, since he has actually looked at frogs\
\[6:16:33 PM\] Jody Garn... says: one second .\
\[6:16:35 PM\] Jody Garn... says: thinking.\
\[6:16:42 PM\] Andrea Ai... says: Here is Roberto too :)\
\[6:17:22 PM\] Jody Garn... says: I think what we would both like is to know what the idea is going forward. From my perspective I would like to know the "focus" of each framework effort.\
\[6:17:31 PM\] Jody Garn... says: So far there is lots in common:\
\[6:17:42 PM\] Roberto C... says: Hi everyone, I will be back a minute. Thanks\
\[6:17:42 PM\] Jody Garn... says: 1. OGC OWS servies ?\
\[6:17:48 PM\] Jody Garn... says: GeoServer yes\
\[6:17:52 PM\] Jody Garn... says: Frogs yes?\
\[6:17:59 PM\] Jody Garn... says: Get? can you guys both answer...\
\[6:18:04 PM\] Jody Garn... says: Post?\
\[6:18:05 PM\] Jody Garn... says: Soap?\
\[6:18:33 PM\] Peter Schut says: FROGS for OGC services - yes\
\[6:18:38 PM\] Peter Schut says: POST yes\
\[6:18:48 PM\] Peter Schut says: SOAP - not yet, but yes eventually\
\[6:18:52 PM\] Chris Holm... says: GeoServer no Soap yet, but should be part of OWS-4\
\[6:18:58 PM\] Jody Garn... says: Okay cool.\
\[6:19:00 PM\] Chris Holm... says: POST and GET yes.\
\[6:19:16 PM\] Jody Garn... says: My next "question" is to do with target audience ...\
\[6:19:31 PM\] Jody Garn... says: GeoServer is hoping to set things up so mid level programers can define new services\
\[6:19:34 PM\] Peter Schut says: GET yes.\
\[6:19:48 PM\] Jody Garn... says: have them hooked up to OGC standards\
\[6:20:06 PM\] Jody Garn... says: and make room for SOAP, WSDL, queue based standards as they are made available.\
\[6:20:16 PM\] Jody Garn... says: without modifying the plugin API,\
\[6:20:31 PM\] Xiaoyuan ... says: Frogs has similar goal too\
\[6:20:34 PM\] Jody Garn... says: ideally we would like a POJO approach, but may have some XML on the sides.\
\[6:20:38 PM\] Peter Schut says: Yes. We want to make it easy to set up new services too, OGC, support SOAP, WSDL.\
\[6:20:50 PM\] Jody Garn... says: Okay cool.\
\[6:20:53 PM\] Jody Garn... says: next question is this.\
\[6:20:56 PM\] Jody Garn... says: Service chaining.\
\[6:21:02 PM\] Jody Garn... says: yes/no or WTF?\
\[6:21:23 PM\] Justin Deo... says: ha, i think we would all love it, but might be a bit out of scope for an initial goal\
\[6:21:25 PM\] Peter Schut says: POJO ? not familiar with it.\
\[6:21:42 PM\] Jody Garn... says: Java beans = Plain Old Java Objects = POJO\
\[6:21:45 PM\] Peter Schut says: Service chainging is enabled with WPS. 4 ways so far....\
\[6:21:53 PM\] Jody Garn... says: using annotations, or reflection to wire it up as a service.\
\[6:22:01 PM\] Peter Schut says: OKOK I know POJO\
\[6:22:30 PM\] Xiaoyuan ... says: both\
\[6:22:38 PM\] Jody Garn... says: GeoServer has not thought about service chaining yet...\
\[6:23:18 PM\] Xiaoyuan ... says: a lot service chaing should be don at client side\
\[6:23:34 PM\] Peter Schut says: I don't see FROGS doing chaining, but WPS does.\
\[6:23:42 PM\] Jody Garn... says: I would argue, leave the data and chaining on the server, and feed the client the result, possibly through a JMQ.\
\[6:23:48 PM\] Jody Garn... says: okay cool.\
\[6:24:11 PM\] Jody Garn... says: Next questions is metadata, intergration, EbRIM or ISO all that kind of stuff.\
\[6:24:24 PM\] Jody Garn... says: Any plans, I know WPS depends on some of it for effective use...\
\[6:24:38 PM\] Jody Garn... says: GeoServer is limping along wanting some other app to provide an editor...\
\[6:25:14 PM\] Jody Garn... says: Guys if we are not there yet, or do not have plans just let me know.\
\[6:25:16 PM\] Peter Schut says: Metadata? Yes service metadata, to support GetCapabilities, plus service administration\
\[6:25:27 PM\] Jody Garn... says: Okay, any support for the metadata uri field?\
\[6:25:29 PM\] Peter Schut says: Integration with what?\
\[6:25:36 PM\] Xiaoyuan ... says: why EbRIM or ISO if you can have xml streams\
\[6:25:44 PM\] Jody Garn... says: or enough information to tie your WMS and WFS together...\
\[6:25:59 PM\] Jody Garn... says: Sorry Xiaoyuan not sure I understood?\
\[6:26:07 PM\] Peter Schut says: ebRIM - not in the cards now. (I can't stand it..., but doesn't mean I'll have to swalllow it sometime...)\
\[6:26:29 PM\] Peter Schut says: ISO where useful. (Read almost never)\
\[6:26:35 PM\] Jody Garn... says: fair enough, all metadata hurts (until you are a client application and need it)\
\[6:26:39 PM\] Chris Holm... says: Of note I think the Catalog 2.0 reference implementation is just going to do ISO, not ebRim.\
\[6:26:47 PM\] Xiaoyuan ... says: getcapabilities stream has more than enough information customized parsing\
\[6:27:10 PM\] Xiaoyuan ... says: We kind of promote xml db or use xml as datatype\
\[6:27:23 PM\] Jody Garn... says: depends on who you talk to, it is easy to blow holes in ISO, but ebRIM is easier at first and they have way more corner cases figured but they show no sign of stopping.\
\[6:27:38 PM\] Peter Schut says: Yes, GetCapabilities is better than WSDL that way - but I think we need both.\
\[6:27:45 PM\] Jody Garn... says: okay next question ...\
\[6:28:00 PM\] Jody Garn... says: Language support (easy one) I know lots of us are Canadian.\
\[6:28:16 PM\] Peter Schut says: Language support - yes\
\[6:28:38 PM\] Jody Garn... says: GeoServer - the user interface yes, capabilies are as you set it up (so no multi language support).\
\[6:28:43 PM\] Peter Schut says: Language will be part of OGC's OWS Common soon.\
\[6:29:06 PM\] Jody Garn... says: harder question: configuration how where is it stored ...\
\[6:29:15 PM\] Peter Schut says: We haven't looked at language for UI, but not against it.\
\[6:29:37 PM\] Xiaoyuan ... says: There is limit on the language support isn't?\
\[6:30:07 PM\] Peter Schut says: I believe our configuration is stored in XML files, but currently read at compile time, not execution. I want to change that if possible.\
\[6:30:10 PM\] Roberto C... says: Configuration stored in XML\
\[6:30:35 PM\] Jody Garn... says: by configuration I was thinking of what the end user can set up?\
\[6:30:50 PM\] Jody Garn... says: you are compliling that in?\
\[6:31:11 PM\] Roberto C... says: Yes, I do have Web Pages to help to cofnigure.\
\[6:32:07 PM\] Jody Garn... says: Question, technical this time.\
\[6:32:12 PM\] Roberto C... says: But, talking about languages. I do support multi-languages with properties files like \_us, \_fr.\
\[6:32:29 PM\] Roberto C... says: It is bundle in the Jar File.\
\[6:32:36 PM\] Jody Garn... says: Has anyone looked into JMX\
\[6:33:05 PM\] Peter Schut says: JMX? Nope.\
\[6:33:10 PM\] Justin Deo... says: a little bit\
\[6:33:13 PM\] Jody Garn... says: we set up geoserver to be configured w/ beans for eventual JMX use (ie configuration console in your application server).\
\[6:33:17 PM\] Justin Deo... says: none of the ui related console stuff\
\[6:33:28 PM\] Jody Garn... says: but we ended up writing a rather effective (but had to maintain) struts app short term\
\[6:33:40 PM\] Jody Garn... says: okay cool.\
\[6:33:53 PM\] Jody Garn... says: One of the things on the OpenSDI list was a goal of a shared configuration\
\[6:33:59 PM\] Jody Garn... says: done as a normal web service.\
\[6:34:11 PM\] Jody Garn... says: The C++ critters like MapServer were game to try that one out as well.\
\[6:34:33 PM\] Jody Garn... says: Okay another hard question: GML3\
\[6:34:44 PM\] Jody Garn... says: (I assume GML2 is easy)\
\[6:34:48 PM\] Peter Schut says: GML3? Aaaarghhhhh!!!!\
\[6:35:11 PM\] Justin Deo... says: well said\
\[6:35:31 PM\] Jody Garn... says: well we got the problem licked :) but need some more hands to get it out the door ...\
\[6:35:32 PM\] Peter Schut says: FROGS doesn't care about GML. WPS can use as an input - but needs something like GeoServer to deal with it.\
\[6:35:49 PM\] Jody Garn... says: <http://udig.refractions.net/confluence/display/OWS3/GTXML+Article>\
\[6:35:57 PM\] Xiaoyuan ... says: any info on binary xml/gml\
\[6:36:10 PM\] Jody Garn... says: waste of time, FastInfo set\
\[6:36:15 PM\] Jody Garn... says: or gzip does you better.\
\[6:36:17 PM\] Justin Deo... says: "GTXML" is a generic XML parsing framework we designed to be scalable enough to handle GML\
\[6:36:19 PM\] Justin Deo... says: 3\
\[6:36:43 PM\] Justin Deo... says: what I would like to see is it tied into the dispatch (request-response) framework so that services dont have to deal with XML directly\
\[6:36:52 PM\] Jody Garn... says: okay we can talk about this later, sharing tech is fun .. on with the questions!\
\[6:36:59 PM\] Jody Garn... says: Q: J2EE tech\
\[6:37:02 PM\] Roberto C... says: I'm using JAXB\
\[6:37:10 PM\] Justin Deo... says: same idea\
\[6:37:16 PM\] Justin Deo... says: well same end goal\
\[6:37:19 PM\] Jody Garn... says: How much, data sources? JXT? JMQ? JMX?\
\[6:37:25 PM\] Justin Deo... says: GTXML is an xml binding technology\
\[6:37:32 PM\] Jody Garn... says: (note article compares JAXB to GTXML for you)\
\[6:37:42 PM\] Jody Garn... says: sigh I fail at moving on as well ...\
\[6:37:53 PM\] Jody Garn... says: Right now GeoServer is at the Servlet stage\
\[6:38:02 PM\] Jody Garn... says: and that is about it. We get pressure to use J2EE data sources\
\[6:38:12 PM\] Jody Garn... says: (so people can use their management console to control our connection pools)\
\[6:38:31 PM\] Jody Garn... says: I see I am babling, any one else got something to add?\
\[6:38:52 PM\] Jody Garn... says: Q: License\
\[6:39:21 PM\] Peter Schut says: J2EE data sources?!? Whatever for?\
\[6:39:45 PM\] Chris Holm... says: Because many people already have their database connections configured.\
\[6:40:04 PM\] Jody Garn... says: (connection pooling, they want us to grab our connections from the Applicatoin Server connection pool)\
\[6:40:12 PM\] Chris Holm... says: Instead of forcing them to also configure through GeoServer, we should be able to just use their existing configurations, that do connection pooling and the like.\
\[6:40:20 PM\] Peter Schut says: FROGS License is Apache.\
\[6:40:32 PM\] Chris Holm... says: We've had a decent number of requests for it over the years.\
\[6:40:33 PM\] Peter Schut says: Oh, I see. How unweblike.\
\[6:40:45 PM\] Jody Garn... says: not sure I understand?\
\[6:41:01 PM\] Jody Garn... says: I think we may be getting wires crossed here.\
\[6:41:20 PM\] Jody Garn... says: But it does answer my questions about intergration w/ normal J2EE technologies vs inventing :)\
\[6:41:29 PM\] Jody Garn... says: (we tend to invent too often)\
\[6:41:38 PM\] Justin Deo... says: i think the point is that we dont want people to have to chagne their entire application stack just to use our framework\
\[6:41:41 PM\] Justin Deo... says: it should slot in seemlessly\
\[6:41:47 PM\] Peter Schut says: Agreed.\
\[6:41:56 PM\] Jody Garn... says: GeoServer is GPL BTW, we are thinking of moving to LGPL for some of the new module work.\
\[6:42:04 PM\] Jody Garn... says: (and keeping GPL modules in places)\
\[6:42:22 PM\] Jody Garn... says: Anyone else with questions?\
\[6:42:49 PM\] Chris Holm... says: Are FROGS guys able to work with GPL or LGPL? Or does it have to be apache?\
\[6:43:29 PM\] Peter Schut says: YOu said you were interested in SPRING\
\[6:43:40 PM\] Jody Garn... says: more then interested\
\[6:43:51 PM\] Jody Garn... says: using it to replace some hacked STRUTS start up code\
\[6:43:57 PM\] Jody Garn... says: and seperate out the code into maven 2 modules.\
\[6:44:04 PM\] Jody Garn... says: (all smushed together at compile time)\
\[6:44:15 PM\] Jody Garn... says: Andrea (possibly asleep) knows more.\
\[6:44:25 PM\] Peter Schut says: We would consider - getting pressure from above - not sure how much work it would be to rewrite FROGS/WPSINT in SPRING\
\[6:44:45 PM\] Andrea Ai... says: I'm not sleeping :)\
\[6:44:52 PM\] Jody Garn... says: strange what would "above" think spring would help?\
\[6:45:11 PM\] Chris Holm... says: Well, to some extent that's what we're doing with GeoServer 1.4 - writing the ogc plug-in framework with spring.\
\[6:45:21 PM\] Peter Schut says: SPRING would standardize - get our enterprise architecture looking the same across different projects.\
\[6:45:36 PM\] Chris Holm... says: So the challenge would mostly be getting WPSInt to play with the spring based framework we're working on.\
\[6:45:48 PM\] Jody Garn... says: R i g h t . . .\
\[6:45:57 PM\] Chris Holm... says: Which is mostly why we want to talk now, to figure out how we can design our spring based stuff to play nicely with your stuff.\
\[6:45:58 PM\] Jody Garn... says: trying to warp my head for a second.\
\[6:46:07 PM\] Peter Schut says: Ecept we've got a fair bit of nice functionality built into FROGS...\
\[6:46:23 PM\] Chris Holm... says: True, so it'd be porting the nice stuff as well.\
\[6:46:43 PM\] Jody Garn... says: Justin do you have a dispatch article you can point them at?\
\[6:46:44 PM\] Andrea Ai... says: I believe he means the Frog's plugin framework\
\[6:46:50 PM\] Chris Holm... says: Could you enumerate what that functionality is, so we have a clearer idea?\
\[6:46:58 PM\] Andrea Ai... says: That's not gonna play with Spring at all due to classloader isolation I fear\
\[6:47:22 PM\] Peter Schut says: Edit OGC service metadata\
\[6:47:40 PM\] Peter Schut says: Validate XML according to WPS input definitions\
\[6:47:56 PM\] Peter Schut says: Publish to CAT\
\[6:48:07 PM\] Peter Schut says: Generic WPS client\
\[6:48:15 PM\] Chris Holm... says: what do you mean by edit ogc service metadata?\
\[6:48:18 PM\] Peter Schut says: Some others I'm forgetting\
\[6:48:21 PM\] Jody Garn... says: (this is where I get confused, WPS works with GML?, and you are using JAXB for that?)\
\[6:48:29 PM\] Andrea Ai... says: Hum, that's stuff you can keep with a Spring based framework as well\
\[6:48:35 PM\] Jody Garn... says: (anwer chris first, technical can be later)\
\[6:48:53 PM\] Peter Schut says: Service metadata to remind administrator what a service is all about, and whether it is public or not\
\[6:49:11 PM\] Roberto C... says: We are not using JAXB for GML but just for our schemas like FROGS Schema, WPS, GDAS, ...\
\[6:49:21 PM\] Andrea Ai... says: So it's hard coded stuff? (the metadata I mean)\
\[6:49:32 PM\] Chris Holm... says: Ok, I'm pretty sure that's in GeoServer as well...\
\[6:49:33 PM\] Jody Garn... says: okay cool\
\[6:49:36 PM\] Peter Schut says: Metadata is editable by the administrator\
\[6:49:41 PM\] Peter Schut says: in a GUI\
\[6:49:49 PM\] Chris Holm... says: What's the gui written with?\
\[6:49:52 PM\] Jody Garn... says: is this configuration?\
\[6:49:59 PM\] Jody Garn... says: that is what I was calling configuration\
\[6:50:03 PM\] Jody Garn... says: (aka of the services)\
\[6:50:34 PM\] Peter Schut says: Yes. configuration. Roberto, what is the GUI written in?\
\[6:50:43 PM\] Roberto C... says: Simple JSP\
\[6:50:55 PM\] Roberto C... says: No struct or something like that\
\[6:51:17 PM\] Jody Garn... says: sweet\
\[6:51:18 PM\] Roberto C... says: and a couple of HTML\
\[6:51:39 PM\] Andrea Ai... says: So the UI is monolithic, or do you have any way to build dinamically the UI from pieces coming from different modules?\
\[6:51:56 PM\] Roberto C... says: Nop\
\[6:51:58 PM\] Chris Holm... says: And that interacts with config objects? Pojo's that can also read from XML? And persist themselves to XML?\
\[6:52:02 PM\] Andrea Ai... says: I know for JSP you can't (at least, you can at build time, not at run time)\
\[6:53:01 PM\] Jody Garn... says: 10 min warning :)\
\[6:53:07 PM\] Jody Garn... says: We should start wrapping things up ...\
\[6:53:17 PM\] Jody Garn... says: So i want to put the "leads" on the spot here ...\
\[6:53:32 PM\] Xiaoyuan ... says: action items?\
\[6:53:37 PM\] Jody Garn... says: Justin do you have any questions, or comments, or things you need to know to move forward.\
\[6:54:06 PM\] Andrea Ai... says: I'd like to investigate a bit more the framework and how Frog wants to leverage Spring\
\[6:54:07 PM\] Justin Deo... says: just that it looks promisitn that we have a lot in common and at this point we havent o verlapped a whole lot\
\[6:54:14 PM\] Justin Deo... says: although the next step for me is to really look at the code\
\[6:54:17 PM\] Andrea Ai... says: Indeed\
\[6:54:33 PM\] Justin Deo... says: unfrotunatley the need for the geoserver spring stuff is pretty urgent here\
\[6:55:00 PM\] Chris Holm... says: It's also promising that your higher ups are also interested in SPRING - could be used as a very excuse for some funded development towards integrating with geoserver.\
\[6:55:01 PM\] Justin Deo... says: but its not really a "framework", its just a modularization, which will help with integration anyways\
\[6:55:11 PM\] Chris Holm... says: since we should do some lead work on spring.\
\[6:55:39 PM\] Peter Schut says: We'll get you our most recent code, but like I said it will take a few more days before we can wrap it up and send it to you.\
\[6:55:55 PM\] Justin Deo... says: no worries, i am up to my eyeballs in work right now\
\[6:56:14 PM\] Justin Deo... says: but if you could get it to me by the end of the week i could spend a few days early next week playing with it\
\[6:56:16 PM\] Peter Schut says: Our move to SPRING may or may not be forced on us - so it's nice to know you are considering it.\
\[6:56:26 PM\] Jody Garn... says: well we are doing it peter\
\[6:56:36 PM\] Jody Garn... says: which should be even nicer to know\
\[6:56:38 PM\] Chris Holm... says: Yeah, more than considering it, it's the current work going right now\
\[6:56:55 PM\] Jody Garn... says: so it a sense I am sad we did not talk to you earlier.\
\[6:56:57 PM\] Chris Holm... says: and why we wanted to check in with you, since it involves moving us more to a 'framework', and wanted to be sure it could work with you.\
\[6:57:12 PM\] Jody Garn... says: Peter can I open the floor to you for questions, comments, etc...\
\[6:57:34 PM\] Peter Schut says: That's fine - I wonder how compatible our stuff is with it. Roberto has agreed to spend some time looking at SPRING when he gets a chance.\
\[6:57:47 PM\] Jody Garn... says: (sorry to be so hard on the agenda and time guys, people stayed late to talk and are going home now)\
\[6:58:12 PM\] Jody Garn... says: So to summarize, volunteer Justin to post the logs :)\
\[6:58:17 PM\] Peter Schut says: Questions, COmments - none for now - just happy we made contact and have a mechanism to chat\
\[6:58:25 PM\] Jody Garn... says: we need to both review code.\
\[6:58:29 PM\] Jody Garn... says: we got a way to chat.\
\[6:58:33 PM\] Peter Schut says: We look forward to working with you!\
\[6:58:55 PM\] Jody Garn... says: Indeed. Thanks to chris for initially moving the projects together.\
\[6:59:07 PM\] Peter Schut says: Do you want us to arrange a demo?\
\[6:59:13 PM\] Justin Deo... says: yeah, this is exciting stuff\
\[6:59:17 PM\] Jody Garn... says: And thanks to Andrea for the initial review and feedback on the FROGs code.\
\[6:59:22 PM\] Peter Schut says: Yes, thanks for pushing, Chris.\
\[6:59:33 PM\] Andrea Ai... says: :)\
\[6:59:33 PM\] Jody Garn... says: lets do this peter, set up the code so we can see it.\
\[6:59:39 PM\] Chris Holm... says: Yeah, I'm psyched this looks like it may work out. Much more promising than other projects I've tried to bring together in the past.\
\[6:59:40 PM\] Jody Garn... says: and we can both arange demos\
\[6:59:45 PM\] Jody Garn... says: and meet two weeks time.\
\[6:59:56 PM\] Chris Holm... says: And if we are successful we'll see big benefits down the line for sure.\
\[6:59:59 PM\] Jody Garn... says: (note this is a deadline for justin so the timing is good, we will have a demo)\
\[7:00:11 PM\] Jody Garn... says: and maybe a few late nights ;(\
\[7:00:36 PM\] Xiaoyuan ... says: Bye! Good luck!\
\[7:00:39 PM\] Jody Garn... says: meeting closed ... thanks all\
\[7:00:44 PM\] Andrea Ai... says: Bye!\
\[7:00:47 PM\] Roberto C... says: Bye! everyone.\
\[7:00:55 PM\] Jody Garn... says: And next time we nede to do introductions !\
\[7:01:00 PM\] Andrea Ai... says: Time to go home for me :)\
\[7:01:01 PM\] Jody Garn... says: my bad.\
\[7:01:03 PM\] Peter Schut says: Cheers!\
\[7:01:16 PM\] \* Xiaoyuan Geng left this chat
