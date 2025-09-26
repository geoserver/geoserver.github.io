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
    response = requests.get(jira_base_url + '/rest/api/2/project/' + jira_project + '/versions', auth=auth)
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
    jql = 'project = ' + jira_project + ' AND fixVersion = "' + version_information['name'] + '" AND resolution IS NOT EMPTY ORDER BY key'
    
    # Fields needed by the application based on usage analysis
    required_fields = [
        'components',      # Used in include_issues() and exclude_issues()
        'issuetype',       # Used in type_names()
        'key',             # Used in templates for issue links
        'summary',         # Used in templates for issue descriptions
        'resolution'       # Used in JQL query logic
    ]
    
    payload = {
        'jql': jql,
        'fields': required_fields,
        'maxResults': 1000
    }
    
    all_issues = []
    next_page_token = None
    
    while True:
        if next_page_token:
            payload['nextPageToken'] = next_page_token
            
        response = requests.post(
            jira_base_url + '/rest/api/3/search/jql', 
            auth=auth, 
            json=payload
        )
        
        if response.status_code != 200:
            response.raise_for_status()
            
        data = response.json()
        all_issues.extend(data.get('issues', []))
        
        next_page_token = data.get('nextPageToken')
        if not next_page_token:
            break
    
    return {'issues': all_issues}


def jira_vulnerability_issues(version_information):
    """
    Query for vulnerability issues using the new disclosure-based approach.
    
    This queries for issues that are either:
    1. Level = Vulnerability (restricted visibility)
    2. Have a Disclosure field set (scheduled for public disclosure)
    3. Component = Vulnerability (legacy approach)
    
    Returns both disclosed and undisclosed vulnerabilities for the given version.
    """
    # Note: level = Vulnerability issues have restricted visibility and may not appear in results
    # until they are disclosed. This is by design for security.
    jql = ('project = ' + jira_project + 
           ' AND fixVersion = "' + version_information['name'] + '"' +
           ' AND resolution IS NOT EMPTY' +
           ' AND (level = Vulnerability OR Disclosure IS NOT EMPTY OR component = Vulnerability)' +
           ' ORDER BY Disclosure DESC')
    
    # Fields needed for vulnerability processing
    required_fields = [
        'components',      # Used for legacy component-based detection
        'issuetype',       # Used in type_names()
        'key',             # Used in templates for issue links
        'summary',         # Used in templates for issue descriptions
        'resolution',      # Used in JQL query logic
        'fixVersions',     # Used in templates for prior blog post updates
        DISCLOSURE_FIELD_ID # Disclosure field (if available)
    ]
    
    payload = {
        'jql': jql,
        'fields': required_fields,
        'maxResults': 1000
    }
    
    all_issues = []
    next_page_token = None
    
    while True:
        if next_page_token:
            payload['nextPageToken'] = next_page_token
            
        response = requests.post(
            jira_base_url + '/rest/api/3/search/jql', 
            auth=auth, 
            json=payload
        )
        
        if response.status_code != 200:
            response.raise_for_status()
            
        data = response.json()
        all_issues.extend(data.get('issues', []))
        
        next_page_token = data.get('nextPageToken')
        if not next_page_token:
            break
    
    return {'issues': all_issues}


def separate_vulnerability_types(vulnerability_issues):
    """
    Separate vulnerability issues into disclosed and undisclosed categories.
    
    Returns:
        tuple: (disclosed_vulnerabilities, undisclosed_vulnerabilities)
    """
    disclosed = []
    undisclosed = []
    
    for issue in vulnerability_issues['issues']:
        # Check if issue has disclosure version set
        disclosure_field = issue['fields'].get(DISCLOSURE_FIELD_ID)  # Disclosure field
        
        if disclosure_field and isinstance(disclosure_field, dict) and disclosure_field.get('released'):
            # If disclosure field is set and the version is released, this is a disclosed vulnerability
            disclosed.append(issue)
        else:
            # No disclosure field set or version not yet released, this is an undisclosed vulnerability
            undisclosed.append(issue)
    
    return disclosed, undisclosed


def jira_disclosure_issues(release_version_name):
    """
    Query for vulnerabilities scheduled for disclosure that match the current release version.
    
    This is used for public disclosure - to find vulnerabilities that should be announced
    with this release based on their disclosure schedule.
    
    Args:
        release_version_name: The release version name (e.g., "2.26.4")
    
    Returns:
        dict: JIRA response containing vulnerabilities scheduled for disclosure
    """
    # Query for vulnerabilities where the disclosure version matches the current release
    jql = ('project IN ("GEOT","GEOS")' +
           ' AND (level = Vulnerability OR component = Vulnerability)' +
           ' AND Disclosure = "' + release_version_name + '"' +
           ' ORDER BY key ASC')
    
    # Fields needed for disclosure processing
    required_fields = [
        'components',      # Used for categorization
        'issuetype',       # Issue type information
        'key',             # Used in templates for issue links
        'summary',         # Used in templates for issue descriptions
        'resolution',      # Resolution status
        'fixVersions',     # Used to identify which releases need updating
        DISCLOSURE_FIELD_ID # Disclosure field
    ]
    
    payload = {
        'jql': jql,
        'fields': required_fields,
        'maxResults': 1000
    }
    
    all_issues = []
    next_page_token = None
    
    while True:
        if next_page_token:
            payload['nextPageToken'] = next_page_token
            
        response = requests.post(
            jira_base_url + '/rest/api/3/search/jql', 
            auth=auth, 
            json=payload
        )
        
        if response.status_code != 200:
            response.raise_for_status()
            
        data = response.json()
        all_issues.extend(data.get('issues', []))
        
        next_page_token = data.get('nextPageToken')
        if not next_page_token:
            break
    
    return {'issues': all_issues}


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


def md_security(vulnerability_list, disclosed_vulnerabilities=None, undisclosed_vulnerabilities=None, urgency_level="important", concurrent_releases=None):
    """
    Generate security section with support for disclosed and undisclosed vulnerabilities.
    
    Args:
        vulnerability_list: Legacy vulnerability list for backward compatibility
        disclosed_vulnerabilities: List of vulnerabilities that are publicly disclosed
        undisclosed_vulnerabilities: List of vulnerabilities not yet disclosed
        urgency_level: Level of urgency - "normal", "important", "urgent"
        concurrent_releases: List of concurrent release versions (e.g., ["2.28.3", "2.26.7"])
    """
    template = templates.get_template('security.md')

    security = template.render(
        vulnerabilities=vulnerability_list,
        disclosed_vulnerabilities=disclosed_vulnerabilities or [],
        undisclosed_vulnerabilities=undisclosed_vulnerabilities or [],
        urgency_level=urgency_level,
        concurrent_releases=concurrent_releases or [],
        jira_base_url=jira_base_url
    )
    print(security, '\n')

def md_community(community_updates):
    template = templates.get_template('community.md')

    community = template.render(community_updates=community_updates,jira_base_url=jira_base_url)
    print(community, '\n')


def md_disclosure(disclosed_vulnerabilities):
    """
    Generate disclosure template for updating prior blog posts.
    
    This generates instructions and text for updating prior release announcements
    when vulnerabilities are being publicly disclosed.
    
    Args:
        disclosed_vulnerabilities: List of vulnerabilities being disclosed
    """
    template = templates.get_template('disclosure.md')

    disclosure = template.render(
        disclosed_vulnerabilities=disclosed_vulnerabilities,
        jira_base_url=jira_base_url
    )
    print(disclosure, '\n')



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
    parser.add_argument("--urgency", help="Security urgency level", type=str,
                        choices=['normal', 'important', 'urgent'], default='important')
    parser.add_argument("--concurrent", help="Concurrent release versions (comma-separated)", type=str)
    parser.add_argument("--disclosure", help="Generate disclosure update for prior blog posts (requires release version, e.g., '2.26.4')", type=str)

    return parser.parse_args()


jira_project = 'GEOS'
jira_base_url = 'https://osgeo-org.atlassian.net'

DISCLOSURE_FIELD_ID = 'customfield_11057'  # Obtained manually from JIRA API

if __name__ == "__main__":
    args = command_line_arguments()
    post = args.post
    security = args.security
    urgency_level = args.urgency
    concurrent_releases = args.concurrent.split(',') if args.concurrent else None
    disclosure_version = args.disclosure
    stable_flag = args.override and args.override == 'stable'
    maintenance_flag = args.override and args.override == "maintenance"

    auth = (args.username, args.password)
    release = args.release

    # Handle disclosure mode - generate prior blog post updates
    if disclosure_version:
        print(f"Generating disclosure updates for vulnerabilities scheduled for disclosure in {disclosure_version}")
        
        file_loader = jinja2.FileSystemLoader('templates')
        templates = jinja2.Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
        
        disclosure_issues = jira_disclosure_issues(disclosure_version)
        
        if len(disclosure_issues['issues']) == 0:
            print(f"No vulnerabilities found scheduled for disclosure in version {disclosure_version}")
            sys.exit(0)
        
        print(f"Found {len(disclosure_issues['issues'])} vulnerabilities scheduled for disclosure:")
        for issue in disclosure_issues['issues']:
            print(f"  - {issue['key']}: {issue['fields']['summary']}")
        
        print("\n" + "="*80)
        md_disclosure(disclosure_issues['issues'])
        sys.exit(0)

    release_type_ = release_type(release, args.override)
    dependency = collaborators(args)
    author = git_user()

    release_versions = jira_series_releases(release)
    release_version = release_versions[0]
    # print(json.dumps(release_version, indent=2))

    project_issues = jira_project_issues(release_version)
    # print(json.dumps(project_issues, indent=2))

    # Query for vulnerability issues using new disclosure-based approach
    vulnerability_issues = jira_vulnerability_issues(release_version)
    disclosed_vulnerabilities, undisclosed_vulnerabilities = separate_vulnerability_types(vulnerability_issues)
    
    # Determine if we have any vulnerabilities (disclosed or undisclosed)
    all_vulnerabilities = disclosed_vulnerabilities + undisclosed_vulnerabilities
    if len(all_vulnerabilities) > 0:
        security = True
    
    # For backward compatibility, still extract vulnerabilities from component-based approach
    # This ensures we don't miss any legacy vulnerability issues
    legacy_vulnerabilities = include_issues(project_issues, 'Vulnerability')
    
    # Combine all vulnerability approaches
    vulnerabilities = all_vulnerabilities if len(all_vulnerabilities) > 0 else legacy_vulnerabilities
        
    community_updates = include_issues(project_issues,'Community modules')
    if len(community_updates) > 0:
        community = True
    else:
        community = False
        
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
            md_security(vulnerabilities, disclosed_vulnerabilities, undisclosed_vulnerabilities, urgency_level, concurrent_releases)

        md_release_notes(release_version, issues, templates)
        
        if community:
            md_community(community_updates)
            
        md_about(release_version, release_versions, templates)

    finally:
        if post:
            sys.stdout.close()
            sys.stdout = stdout_fileno