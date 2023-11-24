#!/usr/bin/python3

import subprocess, os, sys, requests, json, jinja2, argparse


def post_filename(release_version):
    global release
    if not release_version['released']:
        print("release version: " + json.dumps(release_version),file = sys.stderr)
        sys.exit(f'Release {release} not released yet in Jira')
    elif 'releaseDate' not in release_version or not release_version['releaseDate']:
        print("release version: " + json.dumps(release_version),file = sys.stderr)
        sys.exit(f'Release {release} releaseDate not defined in Jira')

    filename = '../_posts/' + release_version['releaseDate'] + \
               '-geoserver-' + release.replace('.','-') + '-released.md'

    if os.path.exists(filename):
        sys.exit(f'File already exists: {filename}')

    return filename


def collaborators(args: argparse.Namespace):
    """
    Process args namespace into map of dependencies for template formatting.

    :param args: Namespace of command line arguments
    :return: map of dependency to version number
    """
    dependencies = []
    if args.geotools:
        dependencies.append(('GeoTools', args.geotools))

    if args.geowebcache:
        dependencies.append(('GeoWebCache', args.geowebcache))

    if args.jai:
        dependencies.append(('JAI-Ext', args.jai))

    if args.imageio:
        dependencies.append(('ImageIO-Ext', args.imageio))

    return dependencies


def jira_series_releases(version_number):
    response = requests.get(jira_base_url + 'rest/api/2/project/' + jira_project + '/versions', auth=auth)
    versions = response.json()

    release_information = None

    for version_information in versions:
        if version_number in version_information['name']:
            release_information = version_information
            break

    if not release_information:
        raise ValueError(f'Version number {version_number} not found')

    series_name = release_information['name'][0:4]
    release_versions = []
    for version_information in versions:
        if ((version_information['name'][0:4] == series_name) and
                version_information['name'] <= release_information['name']):
            release_versions.append(version_information)

    release_versions.sort(key=lambda item: item['name'], reverse=True)

    # for version in releaseVersions:
    #   print( version['name'] + ': '+json.dumps(version))

    return release_versions


def jira_project_issues(version_information):
    jql = 'project = ' + jira_project + ' AND fixVersion = "' + version_information[
        'name'] + '" AND resolution IS NOT EMPTY ORDER BY key'
    params = {'projectId': version_information['projectId'], 'maxResults': 1000, 'jql': jql}
    response = requests.get(jira_base_url + '/rest/api/2/search', auth=auth, params=params)
    return response.json()


def git_user():
    output = subprocess.check_output('git config --global user.name', shell=True)

    return output.decode('utf-8').strip()


def md_header(release_version, series_name, author_name, vulnerability):
    template = templates.get_template('header.md')
    release_name = release_version['name']
    header = template.render(name=release_name,
                             releaseVersion=release_version,
                             series=series_name,
                             author=author_name,
                             vulnerability=vulnerability)
    print(header, '\n')


def md_announcement(release_version, series_name, author_name, dependency, templates):
    release = release_version['name']
    try:
        template = templates.get_template(series_name.replace(' ', '-').lower() + '.md')
    except jinja2.TemplateNotFound:
        template = templates.get_template('announcement.md')

    announcement = template.render(release=release, series=series_name, author=author_name, dependency=dependency)
    print(announcement, '\n')


def include_issues(release_issues,component_name):
    list = []
    for issue in release_issues['issues']:
        issues_components = issue['fields']['components']
        for component in issues_components:
            if component['name'] == component_name:
                list.append(issue)

    return list
    
def exclude_issues(release_issues,component_name):
    list = release_issues['issues'].copy()
    for issue in release_issues['issues']:
        issues_components = issue['fields']['components']
        for component in issues_components:
            if component['name'] == component_name:
                list.remove(issue)

    return list


def md_security(vulnerability_list):
    template = templates.get_template('security.md')

    security = template.render(vulnerabilities=vulnerability_list)
    print(security, '\n')

def md_community(community_updates):
    template = templates.get_template('community.md')

    community = template.render(community_updates=community_updates)
    print(community, '\n')



def type_names(issues):
    issue_types = []
    for issue in issues:
        issue_type = issue['fields']['issuetype']['name']
        if issue_type not in issue_types:
            issue_types.append(issue_type)

    ordered_issue_types = ['New Feature', 'Improvement', 'Bug', 'Task', 'Sub-task']
    for issue_type in ordered_issue_types:
        if issue_type not in issue_types:
            ordered_issue_types.remove(issue_type)

    for issue_type in issue_types:
        if issue_type not in ordered_issue_types:
            ordered_issue_types.append(issue_type)

    return ordered_issue_types


def md_release_notes(release_version, project_issues, templates):
    template = templates.get_template('release_notes.md')

    issue_types = type_names(project_issues)

    release_notes = template.render(release=release_version, issue_type_names=issue_types, project_issues=project_issues,jira_base_url=jira_base_url)
    print(release_notes, '\n')


def md_about(release_version, release_versions, templates):
    series_name = release_version['name'][0:4]
    try:
        template = templates.get_template('about' + series_name[0:1] + series_name[2:] + '.md')
    except jinja2.TemplateNotFound:
        template = templates.get_template('about.md')

    about = template.render(series=series_name, release=release_version, versions=release_versions,jira_base_url=jira_base_url)
    print(about, '\n')


def release_type(version_number, release_type_override):
    """
    Human readable release type determined from version number.

    :param version_number: release version number
    :param release_type_override: release type provided on the command line by the user
    :return: release type: release candidate, milestone, stable, maintenance
    """
    if release_type_override:
        return release_type_override
    elif "RC" in version_number:
        return "release candidate"
    elif "M" in version_number:
        return "milestone"
    elif version_number[5:] < '3':
        return 'stable'
    elif version_number[5:] < '6':
        return 'maintenance'
    else:
        return 'archive'


def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Jira username to access release information")
    parser.add_argument("password", help="Jira credentials to access release information")
    parser.add_argument("release", help="GeoServer release (2.23.0, 2.24-RC, ...)")
    parser.add_argument("--post", help="Generate markdown announcement using release date", action="store_true")
    parser.add_argument("--security", help="Recommended update to address security vulnerability", action="store_true")
    parser.add_argument("--override", help="Override automatic release series", type=str,
                        choices=['stable', 'maintenance', 'archive', 'milestone', 'release candidate'])
    parser.add_argument("--geotools", help="GeoTools version", type=str)
    parser.add_argument("--geowebcache", help="GeoWebCache version", type=str)
    parser.add_argument("--imageio", help="ImageIO-Ext version", type=str)
    parser.add_argument("--jai", help="JAI-Ext version", type=str)

    return parser.parse_args()


jira_project = 'GEOS'
jira_base_url = 'https://osgeo-org.atlassian.net/'

if __name__ == "__main__":
    args = command_line_arguments()
    post = args.post
    security = args.security
    stable_flag = args.override and args.override == 'stable'
    maintenance_flag = args.override and args.override == "maintenance"

    auth = (args.username, args.password)
    release = args.release

    release_type_ = release_type(release, args.override)
    dependency = collaborators(args)
    author = git_user()

    release_versions = jira_series_releases(release)
    release_version = release_versions[0]
    # print(json.dumps(release_version, indent=2))

    project_issues = jira_project_issues(release_version)
    # print(json.dumps(project_issues, indent=2))

    vulnerabilities = include_issues(project_issues,'Vulnerability')
    if len(vulnerabilities) > 0:
        security = True
        
    community_updates = include_issues(project_issues,'Community modules')
    if len(community_updates) > 0:
        community = True
        
    issues = exclude_issues(project_issues,'Community modules')

    file_loader = jinja2.FileSystemLoader('templates')
    templates = jinja2.Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

    stdout_fileno = sys.stdout
    try:
        if post:
            filename = post_filename(release_version)

            print('Generating post to ' + filename)
            print('This is an outline only, some editing will be required!')

            sys.stdout = open(filename, 'w')

        md_header(release_version, release_type_, author, security)
        md_announcement(release_version, release_type_, author, dependency, templates)

        if security:
            md_security(vulnerabilities)

        md_release_notes(release_version, issues, templates)
        
        if community:
            md_community(community_updates)
            
        md_about(release_version, release_versions, templates)

    finally:
        if post:
            sys.stdout.close()
            sys.stdout = stdout_fileno