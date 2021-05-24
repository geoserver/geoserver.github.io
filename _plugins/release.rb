module ReleasePlugin

  class ReleasePageGenerator < Jekyll::Generator
    safe true

    def generate(site)
      p 'release page generator ...'
      site.posts.docs.each do |post|
        if( post.data.has_key?('release'))
          p 'Generating release/'+post.data['version']+' '+post.data['release']+' page'
          site.pages << ReleasePage.new(site, post.data['version'], post)
          
          if( post.data['version'] == site.config['stable_version'] )
            p 'Generating release/stable page'
            site.pages << ReleasePage.new(site, 'stable', post)
          end
          if( post.data['version'] == site.config['maintain_version'] )
            p 'Generating release/maintain page'
            site.pages << ReleasePage.new(site, 'maintain', post)
          end
          if( post.data['version'] == site.config['dev_version'] )
            p 'Generating release/dev page'
            site.pages << ReleasePage.new(site, 'dev', post)
          end
        end
      end
      
      if( ! site.config['dev_version'] )
         p 'Generating release/dev placeholder'
         dev = NightlyPage.new(
           site, 
           site.config['dev_branch'],
           site.config['dev_series'][0..-3],
           'latest',
           site.config['dev_jira']
         )
         dev.dir = 'release/dev'
         site.pages << dev
      end
      
      p 'Generating release/main page'
      site.pages << NightlyPage.new(
        site, 
        site.config['dev_branch'],
        site.config['dev_series'][0..-3],
        'latest',
        site.config['dev_jira']
      )
      
      
      p 'Generating release/'+site.config['stable_branch']+' page'
      site.pages << NightlyPage.new(
        site, 
        site.config['stable_branch'],
        site.config['stable_branch'][0..-3],
        'stable',
        site.config['stable_jira']
      )
      
      p 'Generating release/'+site.config['maintain_branch']+' page'
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
        'jira_version' => post.data['jira_version'],
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