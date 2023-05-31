#!/usr/bin/python3

# Requires python 3.10+ for match syntax
#
# Reference: https://community.atlassian.com/t5/Jira-Software-questions/Is-there-a-way-to-use-the-JIRA-API-to-retrieve-Release-Notes-of/qaq-p/1678046

import subprocess, os, sys, requests, json, jinja2, argparse

def releaseName(release):
    return release['name']

def postFilename(releaseVersion):
   if not releaseVersion['released']:
     print('Release '+release+' not released yet in Jira')
     print(json.dumps(releaseVersion))
     exit()
 
   elif 'releaseDate' not in releaseVersion or not releaseVersion['releaseDate']:
     print('Release '+release+' releaseDate not defined in Jira')
     print(json.dumps(releaseVersion))
     exit()

   filename = '../_posts/'+releaseVersion['releaseDate']+'-geoserver-'+release.replace('.','-')+'-released.md'
  
   if os.path.exists(filename):
      print('File already exists: '+filename)
      exit()
   
   return filename
   
def getDependencies(args):
   dependencies = []
   if args.geotools:
      dependencies.append( ('GeoTools', args.geotools) )
      
   if args.geowebcache:
      dependencies.append( ('GeoWebCache', args.geowebcache) )

   if args.jai:
      dependencies.append( ('JAI-Ext', args.jai) )
      
   if args.imageio:
      dependencies.append( ('ImageIO-Ext', args.imageio) )
   
   return dependencies
 

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

def mdHeader(releaseVersion,series,author,security):
   template = env.get_template('header.md')
   name = releaseVersion['name']
   header = template.render(name=name,releaseVersion=releaseVersion,series=series,author=author,vulnerability=security)
   print(header,'\n')
    
#def mdHeader(releaseVersion,series,author,secuirty):
#    name = releaseVersion['name']
#    print('---')
#    print('author: '+author)
#    print('layout: post')
#    print('title: GeoServer '+name+' Released')
#    print('categories:')
#    print(' - Announcements')
#    print('tags:')
#    
#    print(series)
#    
#    match series:
#       case 'release candidate':
#          print('- Release Candidate')
#       case 'milestone':
#          print('- Milestone Release')
#       case _:
#          print('- Release')
#    
#    if secuirty:
#       print('- Vulnerability')
#       
#    print('release: release_'+name[0:1]+''+name[2:4])
#    print('version: '+name)
#    print('jira_version: '+releaseVersion['id'])
#    print('---')

def mdAnouncement(releaseVersion, series, author, dependency, env):
   release = releaseVersion['name']
   try:
      template = env.get_template(series.replace(' ','-').lower()+'.md')
   except:
      template = env.get_template('announcement.md')
   
   anouncement = template.render(release=release,series=series,author=author,dependency=dependency)
   print(anouncement,'\n')

def getVulnerabilities(releaseIssues):
   vulnerabilities = []
   for issue in releaseIssues['issues']:
       commponents = issue['fields']['components']
       for component in commponents:
          if component['name'] == 'Vulnerability':
              vulnerabilities.append(issue)
              
   return vulnerabilities
   
def mdSecurity(vulnerabilities):
   template = env.get_template('security.md')
   
   security = template.render(vulnerabilities=vulnerabilities)
   print(security,'\n')

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

def mdReleaseNotes(releaseVersion, projectIssues, env):
    template = env.get_template('release_notes.md')
    
    issueTypeNames = collectIssueTypeNames(projectIssues['issues'])
    
    release_notes = template.render(release=releaseVersion,issueTypeNames=issueTypeNames,projectIssues=projectIssues)
    print(release_notes,'\n')

def mdAbout(releaseVersion, releaseVersions, env):
    series=releaseVersion['name'][0:4]
    try:
       template = env.get_template('about'+series[0:1]+series[2:]+'.md')
    except:
       template = env.get_template('about.md')
    
    about = template.render(series=series,release=releaseVersion,versions=releaseVersions)
    print(about)

def getSeries(release, override):
   if override:
      return override
   elif "RC" in release:
      return "release candidate"
   elif "M" in release:
      return "milestone"
   elif release[5:] < '3':
      return 'stable'
   elif release[5:] < '6':
      return 'maintenance'
   else:
      return 'archive'

# def series(name, stable, maintenance):
#    if stable:
#       return 'stable'
#    elif maintenance:
#       return 'maintenance'
#    elif "RC" in name:
#       return "release candidate"
#    elif "M" in name:
#       return "milestone"
#    elif name[5:] < '3':
#       return 'stable'
#    elif name[5:] < '6':
#       return 'maintenance'
#    else:
#       return 'archive'

project = 'GEOS'
jiraBaseUrl = 'https://osgeo-org.atlassian.net/'

parser = argparse.ArgumentParser()
parser.add_argument("username",help="Jira username to access release information")
parser.add_argument("password",help="Jira credentials to access release information")
parser.add_argument("release",help="GeoServer release (2.23.0, 2.24-RC, ...)")
parser.add_argument("--post", help="Generate markdown anouncement using release date",action="store_true")
parser.add_argument("--security", help="Recommended update to address security vulnerability",action="store_true")
parser.add_argument("--override", help="Override automatic release series",type=str,choices=['stable', 'maintenance', 'archive','milestone','release candidate'])
parser.add_argument("--geotools", help="GeoTools version",type=str)
parser.add_argument("--geowebcache", help="GeoWebCache version",type=str)
parser.add_argument("--imageio", help="ImageIO-Ext version",type=str)
parser.add_argument("--jai", help="JAI-Ext version",type=str)

args = parser.parse_args()
post = args.post
security = args.security
stable = args.override and args.override == 'stable'
maintenance = args.override and args.override == "maintenance"

auth=(args.username, args.password)
release = args.release

series = getSeries(release,args.override)
dependency = getDependencies(args)
author = gitUser()

releaseVersions = getSeriesReleasesFromNamePart(release)
releaseVersion = releaseVersions[0]
# print(json.dumps(projectVersion, indent=2))

projectIssues = getProjectIssuesFromVersion(releaseVersion)
# print(json.dumps(projectIssues, indent=2))

vulnerabilities = getVulnerabilities(projectIssues)
if len(vulnerabilities) > 0:
   security = True

file_loader = jinja2.FileSystemLoader('templates')
env = jinja2.Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)

stdout_fileno = sys.stdout
try:
   if post:
      filename = postFilename(releaseVersion)
   
      print('Generating post to '+filename)
      print('This is an outline only, some editing will be required!')
   
      sys.stdout = open(filename, 'w')

   mdHeader(releaseVersion,series,author,security)

   mdAnouncement(releaseVersion,series,author,dependency,env)

   if security:
     mdSecurity(vulnerabilities)

   mdReleaseNotes(releaseVersion, projectIssues, env)

   mdAbout(releaseVersion,releaseVersions,env)

finally:
   if post:
      sys.stdout.close()
      sys.stdout = stdout_fileno