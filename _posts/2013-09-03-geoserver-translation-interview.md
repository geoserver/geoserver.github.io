---
author: geoserver
comments: true
date: 2013-09-03 10:33:18+00:00
layout: post
link: http://blog.geoserver.org/2013/09/03/geoserver-translation-interview/
slug: geoserver-translation-interview
title: GeoServer Translation Interview with Frank Gasdorf
wordpress_id: 1546
categories:
- Behind The Scenes
tags:
- localization
- translate
- ui
---

_Here is an unusual post for the GeoServer blog - an interview! We have been asking [Frank Gasdorf](http://twitter.com/fgdrf1976) to write a blog post, to thank all the amazing translators, for some time. Finally in an act of desperation Jody managed to hunt him down on Skype for a few questions on how GeoServer translation works and how you can get involved._

**Q: So frank I am used to working with you on uDig or the Live DVD. When did you start with GeoServer?**

Let me try to answer. My first contact with all these open source projects was in 2008 - with uDig as I used to use at work as a platform for our GIS system.

uDig is a desktop application with uses OGC services (WFS, WMS and whatever) therefore we needed to use GeoServer and MapServer. And we chose GeoServer as we were familiar with the GeoTools library.

**Q: When did you start getting involved as a committer with GeoServer?**

Around about two years ago, I have no idea maybe we can check. I think it was about Wicket and the UI and some missing externalized strings - so we can translate it into German.

**Q: Ah so you started out with GeoServer and translation from the get go.**

Yes. GeoServer was still using subversion, and we requested commit access. We had to show were familiar with GeoServer build, issue tracker and so on.

**Q: Was that difficult?**

Not really, always had a guiding hand from the mailing list, committers and my questions were answered quickly.

**Q: I want to ask you about all the amazing translation work you have set up, every release seems to have more languages coming on board. How do you do it?**

We had several stages of success. First part everything was about finding an easy-to-use crowd platform for translations with support to synchronize from and back to the core code base. The second step was about setting up the environment for several resources identified as translatable UI elements. And finally we initially set up languages teams everybody can join after approval.

While posting the progress on Twitter, [Google+ GeoServer Community](https://plus.google.com/communities/101905665894825745986) or massages on the Mailing-list the community of translators has grown rapidly from few translators during 2.1.x release cycles to currently around 80 for release train 2.4.x.

We started with the GeoServer 2.1 with 15 resources and set up the main languages and some others already existed from other translation platforms or in source repository of GeoServer.

Now GeoServer is up to 25 translations, with a total of 25 resources to translate.

**Q: Hold on what is a resource you are going too fast.**

A resource is like a text file, where the developers have separated out all the human readable text from the applications user interface. Like dialogs, table headers and forms.

Here is an example from the web-wms module:

    
    <code><small>AbstractStylePage.confirmOverwrite = Really want to overwrite the current editor contents?
    AbstractStylePage.copy             = Copy ...
    AbstractStylePage.copyFrom         = Copy from existing style
    </small></code>


**Q: In each release you have been showing these great graphs illustrating the progress translating into different languages. Where are those from?**

[![](/img/uploads/TransifexCurrentState1.png)](http://blog.geoserver.org/2013/09/03/geoserver-translation-interview/transifexcurrentstate/)



The screens are taken from the Transifex platform, which you can see at the following link:

[https://www.transifex.com/projects/p/geoserver_stable](https://www.transifex.com/projects/p/geoserver_stable/)

The content is stored in the cloud and the platform allows you to host translations for open source projects for free. Different plans for commercial and open source projects.

As long as these projects are publicly accessible, and the core project is open source, the service is free.

**Q: Can you show me what translating looks like?**

Well you can probably login with Facebook or other social accounts. Have a look.

**Q: Yeah that worked (it did Twitter, Google, Facebook) and I can now go in and view the French translation.**

[![](/img/uploads/translate-fr-300x159.png)](/img/uploads/translate-fr.png)

That is it - the translation screen is similar, but you would be allowed edit the string.

To edit you have to request to join the organization, when you have joined there is different roles: Administrator, Translator and Reviewer.

**Q: So how do people contact you to help out translating GeoServer?**

There are two different ways people join:



	
  1. For existing languages they can join a translation team, for e.g. Italian

	
  2. If a translation team does not exist yet they request a new language team for GeoServer project.


This month Thai, Indonesian and Vietnamese teams were set up!

**Q: Wow that is amazing, do they have to sign a code license agreement like code committers, or are you putting this in on their behalf?**

Right now we team up with GeoServer committers to bring the translations back to the code base. The Transifex platform has a nice feature for CLA agreements. Once users request to join a Team, they have to accept the CLA. Only who accepted the CONTRIBUTOR ASSIGNMENT AGREEMENT_ _ is allowed to edit.

**Q: Is this the same technology you use for the Live DVD?**

Not yet, but we are considering it. Actually there isn't any support for Restructured Text available at the moment.

**Q: How are the translations being received by the community? We obviously do not get a lot of feedback on geoserver-devel which is an english email list.**

The developers can mostly speak English and prefer to work with GeoServer in English. In the emerging world users only speak their own language and therefore they have no access of open source projects or capabilities. If it is not translated it is not usable. Another hurdle may be the lack of knowledge about developing tools and infrastructure. Translators are mostly Users and not Developers, who knows how to checkout, modify and push back changes from and into a source repository.

Translators form a bridge between the users and the developers allowing open source to be used in their own language.

I direct message that can answer that question:

[![](/img/uploads/TwitterMessage1.png)](http://blog.geoserver.org/2013/09/03/geoserver-translation-interview/twittermessage/)



















I would like to thank all these amazing guys who have been contributing 25 languages at the moment. Special Thanks goes to [Oscar Fonts](https://www.transifex.com/accounts/profile/oscar.fonts), who helped a lot during project initialization phase and describing synchronization workflows.

There are many other people - especially all team coordinators - who made it a success so far:

[AlexGacon](https://www.transifex.com/accounts/profile/AlexGacon/),[BelloWaff](https://www.transifex.com/accounts/profile/BelloWaff/),[engingem](https://www.transifex.com/accounts/profile/engingem/),[fgdrf](https://www.transifex.com/accounts/profile/fgdrf/),[fphg](https://www.transifex.com/accounts/profile/fphg/),[ipotalamo](https://www.transifex.com/accounts/profile/ipotalamo/),[isoarpa](https://www.transifex.com/accounts/profile/isoarpa/),[Lasnei](https://www.transifex.com/accounts/profile/Lasnei/),[mapplus](https://www.transifex.com/accounts/profile/mapplus/),[oscar.fonts](https://www.transifex.com/accounts/profile/oscar.fonts/),[PauliusL](https://www.transifex.com/accounts/profile/PauliusL/),[ppanhh](https://www.transifex.com/accounts/profile/ppanhh/),[TheLooka](https://www.transifex.com/accounts/profile/TheLooka/),[vladimir_r](https://www.transifex.com/accounts/profile/vladimir_r/),

[xurxosanz](https://www.transifex.com/accounts/profile/xurxosanz/),[yecarrillo](https://www.transifex.com/accounts/profile/yecarrillo/),[bartvdebartvde](https://www.transifex.com/accounts/profile/bartvde/), [bchartierbchartier](https://www.transifex.com/accounts/profile/bchartier/), [BEignerBEigner](https://www.transifex.com/accounts/profile/BEigner/),[BesandBesand](https://www.transifex.com/accounts/profile/Besand/),[cbredelcbredel](https://www.transifex.com/accounts/profile/cbredel/),[csorincsorin](https://www.transifex.com/accounts/profile/csorin/),[cuneytoktaycuneytoktay](https://www.transifex.com/accounts/profile/cuneytoktay/),

[DavorRaci?](https://www.transifex.com/accounts/profile/DavorRaci%C4%87/),[diegospsdiegosps](https://www.transifex.com/accounts/profile/diegosps/),[dkusicdkusic](https://www.transifex.com/accounts/profile/dkusic/),[emacgillavryemacgillavry](https://www.transifex.com/accounts/profile/emacgillavry/),[ErenConErenCon](https://www.transifex.com/accounts/profile/ErenCon/),[felix.liberiofelix.liberio](https://www.transifex.com/accounts/profile/felix.liberio/),[franz_erifranz_eri](https://www.transifex.com/accounts/profile/franz_eri/),

[fvanderbiestfvanderbiest](https://www.transifex.com/accounts/profile/fvanderbiest/),[gaiyonggaiyong](https://www.transifex.com/accounts/profile/gaiyong/),[GeographyGeography](https://www.transifex.com/accounts/profile/Geography/),[groldangroldan](https://www.transifex.com/accounts/profile/groldan/),[hanchaohanchao](https://www.transifex.com/accounts/profile/hanchao/),[hiroshi.harimoto.1hiroshi.harimoto.1](https://www.transifex.com/accounts/profile/hiroshi.harimoto.1/),

[HugoMartinsHugoMartins](https://www.transifex.com/accounts/profile/HugoMartins/),[ibitzibitz](https://www.transifex.com/accounts/profile/ibitz/),[jls2933jls2933](https://www.transifex.com/accounts/profile/jls2933/),[jorn.vegard.rosnesjorn.vegard.rosnes](https://www.transifex.com/accounts/profile/jorn.vegard.rosnes/),[JRMJRM](https://www.transifex.com/accounts/profile/JRM/),[juasmillajuasmilla](https://www.transifex.com/accounts/profile/juasmilla/),[kalxaskalxas](https://www.transifex.com/accounts/profile/kalxas/),

[kazuyonagahamakazuyonagahama](https://www.transifex.com/accounts/profile/kazuyonagahama/),[kiu.sou1kiu.sou1](https://www.transifex.com/accounts/profile/kiu.sou1/),[kladesskladess](https://www.transifex.com/accounts/profile/kladess/),[k.muramatsuk.muramatsu](https://www.transifex.com/accounts/profile/k.muramatsu/),[kullervo1892kullervo1892](https://www.transifex.com/accounts/profile/kullervo1892/),

[lazareveugenelazareveugene](https://www.transifex.com/accounts/profile/lazareveugene/),[lluis.rl.1996lluis.rl.1996](https://www.transifex.com/accounts/profile/lluis.rl.1996/),[loic_geobretagneloic_geobretagne](https://www.transifex.com/accounts/profile/loic_geobretagne/),[MangoWoongMangoWoong](https://www.transifex.com/accounts/profile/MangoWoong/),

[mapconciergemapconcierge](https://www.transifex.com/accounts/profile/mapconcierge/),[mapconcierge_facebookmapconcierge_facebook](https://www.transifex.com/accounts/profile/mapconcierge_facebook/),[marceloboeiramarceloboeira](https://www.transifex.com/accounts/profile/marceloboeira/),

[MarceloThomazMarceloThomaz](https://www.transifex.com/accounts/profile/MarceloThomaz/),[marcjansenmarcjansen](https://www.transifex.com/accounts/profile/marcjansen/),[MehmanMehman](https://www.transifex.com/accounts/profile/Mehman/),[miblonmiblon](https://www.transifex.com/accounts/profile/miblon/),[miki.okano.106miki.okano.106](https://www.transifex.com/accounts/profile/miki.okano.106/),

[msokomsoko](https://www.transifex.com/accounts/profile/msoko/),[netinhonetinho](https://www.transifex.com/accounts/profile/netinho/),[nyampirenyampire](https://www.transifex.com/accounts/profile/nyampire/),[oememoemem](https://www.transifex.com/accounts/profile/oemem/),[phiocouekphiocouek](https://www.transifex.com/accounts/profile/phiocouek/),[pmgmendespmgmendes](https://www.transifex.com/accounts/profile/pmgmendes/),[procarrieprocarrie](https://www.transifex.com/accounts/profile/procarrie/),

[rodrod](https://www.transifex.com/accounts/profile/rod/),[sanada_kazushisanada_kazushi](https://www.transifex.com/accounts/profile/sanada_kazushi/),[SeanParkSeanPark](https://www.transifex.com/accounts/profile/SeanPark/),[shimiyushimiyu](https://www.transifex.com/accounts/profile/shimiyu/),[taudorftaudorf](https://www.transifex.com/accounts/profile/taudorf/),[thanhlvthanhlv](https://www.transifex.com/accounts/profile/thanhlv/),[ulysseskaoulysseskao](https://www.transifex.com/accounts/profile/ulysseskao/),

[vistonevistone](https://www.transifex.com/accounts/profile/vistone/),[westriver1990westriver1990](https://www.transifex.com/accounts/profile/westriver1990/),[wiselymanwiselyman](https://www.transifex.com/accounts/profile/wiselyman/),[woutervannifterickwoutervannifterick](https://www.transifex.com/accounts/profile/woutervannifterick/),[xuyongfsxuyongfs](https://www.transifex.com/accounts/profile/xuyongfs/),

[you.kudo.5you.kudo.5](https://www.transifex.com/accounts/profile/you.kudo.5/),[????????](https://www.transifex.com/accounts/profile/%E7%9B%B8%E5%B3%B6%E5%81%A5%E4%BB%8B/)

Thank you for giving me the chance to talk about it and I hope I'll meet some of you at [FOSS4G](http://2013.foss4g.org/) in Nottingham.

**Q: That is right there is a GeoServer code-sprint - where can people sign up?**

On the OSGeo wiki [FOSS4G 2013 Code Sprint](http://wiki.osgeo.org/wiki/FOSS4G_2013_Code_Sprint#GeoServer) scroll down to the GeoServer entry and add your name.

**
**

**
**
