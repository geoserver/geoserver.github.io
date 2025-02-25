module ReleasePlugin

  class ReleasePageGenerator < Jekyll::Generator
    safe true

    def generate(site)
      releases = Hash[]
      
      p 'release page generator ...'
      site.posts.docs.each do |post|
        if( post.data.has_key?('release'))
          version = post.data['version']
          series = version.scan(/^(\d+)\.(\d+)/).join('.')
          
          if( releases.key?(series) )
             releases[series].push( version )
          else
             releases[series] = [version]
          end
          
          # p '  Generating release/'+version+' '+post.data['release']+' page'
          site.pages << ReleasePage.new(site, version, post)
        end
      end
      site.data['releases'] = releases
      
      # Can we determine latest stable and maintenance page?
      p 'Review posts to identify latest releases'
      for item in releases
         if item[0] == site.config['dev_branch'].chomp('.x')
           dev_latest = item[1].last
           p '  Identify dev_version=' + dev_latest
           site.config['dev_version'] = dev_latest
         elsif item[0] == site.config['stable_branch'].chomp('.x')
           stable_latest = item[1].last
           p '  Identify stable_version=' + stable_latest
           site.config['stable_version'] = stable_latest
         elsif item[0] == site.config['maintain_branch'].chomp('.x')
           maintain_latest = item[1].last
           p '  Identify maintain_version=' + maintain_latest
           site.config['maintain_version'] = maintain_latest
         end
      end
      
      # look up latest deatils
      p 'Review posts to identify latest release jira details and publish placeholder pages'
      
      site.posts.docs.each do |post|
        version = post.data['version']
        if post.data.has_key?('release')
          if version == site.config['stable_version']
             site.config['stable_jira'] = post.data['jira_version']
             p '  Identify ' + post.data['title'] +' stable_jira=' + site.config['stable_jira'].to_s
             p '  Generating release/stable page for ' + version
             site.pages << ReleasePage.new(site, 'stable', post)
          elsif version == site.config['maintain_version']
             site.config['maintain_jira'] = post.data['jira_version']
             p '  Identify ' + post.data['title'] +' maintain_jira=' + site.config['maintain_jira'].to_s
             p '  Generating release/maintain page for '+ version
             site.pages << ReleasePage.new(site, 'maintain', post)
          elsif version == site.config['dev_version']
             site.config['dev_jira'] = post.data['jira_version']
             p '  Identify ' + post.data['title'] +' dev_jira=' + site.config['dev_jira'].to_s
             p '  Generating release/dev page for ' + version
             site.pages << ReleasePage.new(site, 'dev', post)
          end
        end
      end
           
      p 'Generating release/main nightly page'
      site.pages << NightlyPage.new(
        site, 
        'main',
        site.config['main_series'][0..-3],
        'latest',
        site.config['main_jira']
      )
      
      if (site.config['dev_branch'] != 'main' )
        p 'Generating release/'+site.config['dev_branch']+' nightly page dev_jira ' + site.config['dev_jira'].to_s
        site.pages << NightlyPage.new(
          site, 
          site.config['dev_branch'],
          site.config['dev_branch'][0..-3],
          site.config['dev_branch'],
          site.config['dev_jira']
        )
      end
      
      if( ! site.config['dev_version'] )
         p 'Generating release/dev nightly for '+site.config['dev_branch']+' dev_jira='+site.config['dev_jira'].to_s
         dev = NightlyPage.new(
           site, 
           site.config['dev_branch'],
           site.config['dev_branch'][0..-3],
           'latest',
           site.config['dev_jira']
         )
         dev.dir = 'release/dev'
         site.pages << dev
      end
      
      p 'Generating release/'+site.config['stable_branch']+' nightly page stable_jira='+site.config['stable_jira'].to_s
      site.pages << NightlyPage.new(
        site, 
        site.config['stable_branch'],
        site.config['stable_branch'][0..-3],
        'stable',
        site.config['stable_jira']
      )
      
      p 'Generating release/'+site.config['maintain_branch']+' nightly page maintain_jira='+site.config['maintain_jira'].to_s
      site.pages << NightlyPage.new(
        site, 
        site.config['maintain_branch'],
        site.config['maintain_branch'][0..-3],
        'maintain',
        site.config['maintain_jira']
      )
    end
  end

  # Subclass of `Jekyll::PageWithoutAFile` configured as a download page
  class ReleasePage < Jekyll::PageWithoutAFile 
    def initialize(site, release, post)
      super(site, site.source, 'release/'+release, 'index.html')
      
      @site = site               # the current site instance.
      @base = site.source        # path to the source directory.
      @dir  = 'release/'+release # the directory the page will reside in.

      # All release pagess have the same filename, so define attributes straight away.
      @basename = 'index'      # filename without the extension.
      @ext      = '.html'      # the extension.
      @name     = 'index.html' # basically @basename + @ext.
      
      # This stuff used to be in the individual release/2.19.1/index.html file
      @data = {
        'layout' => post.data['release'],
        'title' => 'GeoServer',
        'version' => post.data['version'],
        'series' => post.data['version'].scan(/^(\d+)\.(\d+)/).join('.'),
        'jira_version' => post.data['jira_version'],
        'doi' => post.data['doi'],
        'release_date' => post.data['date'].strftime("%B %e, %Y"),
        'announce' => post.url,
      }
    end
  end
  
  # Subclass of `Jekyll::PageWithoutAFile` configured as a nightly build
  class NightlyPage < Jekyll::PageWithoutAFile 
    def initialize(site, version, series, docs, jira_version)
      super(site, site.source, 'release/'+version, 'index.html')
      
      @site = site               # the current site instance.
      @base = site.source        # path to the source directory.
      @dir  = 'release/'+version # the directory the page will reside in.

      # All release pagess have the same filename, so define attributes straight away.
      @basename = 'index'      # filename without the extension.
      @ext      = '.html'      # the extension.
      @name     = 'index.html' # basically @basename + @ext.
      
      # This stuff used to be in the individual release/2.19.1/index.html file
      @data = {
        'layout' => 'nightly',
        'title' => 'GeoServer',
        'version' => version,
        'jira_version' => jira_version,
        'branch_name' => version,
        'docs' => docs,
        'branch' => version,
        'series' => series
      }
    end
  end
  
end