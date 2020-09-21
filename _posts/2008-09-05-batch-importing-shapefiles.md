---
author: bmmpxf
comments: true
date: 2008-09-05 14:49:18+00:00
layout: post
link: http://blog.geoserver.org/2008/09/05/batch-importing-shapefiles/
slug: batch-importing-shapefiles
title: Batch Importing Shapefiles (The Adventure)
wordpress_id: 122
categories:
- Tips and Tricks
---

If you've ever needed to import multiple shapefiles into GeoServer, you  know that currently there aren't any built-in tools to let you to do  this.  I had to import about a hundred of them for some work I was  doing, and it simply wasn't feasible to do them one at a time.  (Recall  that shapefiles are their own DataStores, so one needs to set up DataStores and FeatureTypes for each shapefile, in effect double the work compared to a database.)  I polled the users mailing  list but didn't get much of a response, aside from others looking for  the same.

Impetuously, I decided to set out to solve this problem myself. <!-- more --> I am by  no means a programmer (at least not yet), but I have some shell/batch scripting  history, and was, as [Hunter Thompson](http://en.wikipedia.org/wiki/Hunter_S._Thompson) once said, “just sick enough to be  totally confident.”  I decided to write a batch import program in  Python, if for no other reason than we have some sophisticated  Python developers in the office, so I figured I was in good hands.  Yes,  I didn't actually have any Python experience per se, which sort of  likened the experience to someone who has never held a soldering iron building a personal computer.

So, I tweaked, tinkered, read [Learning Python](http://oreilly.com/catalog/9780596513986/), asked a ton of questions  to my tireless office mates, and in a short eternity had a script that  did the following:



	
  1. Copied a shapefile (and associated files) to the data directory

	
  2. Appended info block to catalog.xml

	
  3. Created named FeatureType directory and associated info.xml


Some parts of the process were made easy in my particular case.  All my  SLDs were already loaded into the data directory, with the same name as the shapefile.  Every shapefile had the same bounding box, projection, and  namespace, so I could hard code those into the script without having to  figure out how to get at them another way.  The script  wasn't pretty, but it worked, and to me, that was the most important part.

The punchline to this story is that **the very next day** after I got all  my shapefiles loaded, there appeared a [response to my initial query](http://www.nabble.com/shp2geoserver:-batch-import-for-shapefiles-td18189529.html),  wherein a kind soul had posted a python script that did (approximately) the exact same  thing.

Stoyan Shopov from [LISAsoft](http://lisasoft.com/), a geospatial software and consulting  company, was in the same situation as I was.  He created the script, as he says, “by  my own initiative and out of frustration,” which pretty much sums it  up.  His script was, of course, miles ahead of mine in compactness and  sheer elegance.  That said, in the spirit of open-source and sharing  that is our solemn creed, I offer both mine and Stoyan's scripts (with  his permission, of course).

[Download Stoyan's script](http://blog.geoserver.org/wp-content/uploads/shp2geoserver.py)
[Download my script](http://blog.geoserver.org/wp-content/uploads/shapefilebatch-cleaned.py) (_Warning: If you are a Python programmer, you may be  horrified._)

Now, eventually a lot of this work will be obsolete, as the GeoServer  developers are working on a [RESTful interface](http://geoserver.org/display/GEOSDOC/RESTful+Configuration+API) that will allow for easy  configuration changes from a command line.  I have seen a demo of this  functionality, and it is impressive in its simplicity and its  why-didn't-they-do-this-sooner-ness.

Are there any interesting scripts or external programs you have employed  when working with GeoServer?  If so, then speak up, as there's a good  chance that someone is encountering that very problem you've already  solved.

_Note: Comments have been restored to this blog after a long absence, so your comments will no longer be lost in the void.  Thanks for your patience on this one._
