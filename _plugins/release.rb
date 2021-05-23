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
         
         dev = Jekyll::PageWithoutAFile.new( site, site.source, 'release/dev', 'index.html');
         dev.data = {
             'layout' => 'nightly',
             'title' => 'GeoServer',
             'version' => '',
             'jira_version' => site.config['dev_jira'],
             'branch_name' => 'main',
             'docs' => 'latest',
             'branch' => 'main',
             'series' => site.config['dev_series'],
         }
         site.pages << dev
      end
      
      p 'Generating release/main page'
      dev = Jekyll::PageWithoutAFile.new( site, site.source, 'release/main', 'index.html');
      dev.data = {
          'layout' => 'nightly',
          'title' => 'GeoServer',
          'version' => '',
          'jira_version' => site.config['dev_jira'],
          'branch_name' => 'main',
          'docs' => 'latest',
          'branch' => 'main',
          'series' => site.config['dev_series'][0..-3],
      }
      site.pages << dev
      
      p 'Generating release/'+site.config['stable_branch']+' page'
      dev = Jekyll::PageWithoutAFile.new( site, site.source, 'release/'+site.config['stable_branch'], 'index.html');
      dev.data = {
          'layout' => 'nightly',
          'title' => 'GeoServer',
          'version' => site.config['stable_branch'],
          'jira_version' => site.config['stable_jira'],
          'branch_name' => site.config['stable_branch'],
          'docs' => 'stable',
          'branch' => site.config['stable_branch'],
          'series' => site.config['stable_branch'][0..-3],
      }
      site.pages << dev
      
      p 'Generating release/'+site.config['maintain_branch']+' page'
      dev = Jekyll::PageWithoutAFile.new( site, site.source, 'release/'+site.config['maintain_branch'], 'index.html');
      dev.data = {
          'layout' => 'nightly',
          'title' => 'GeoServer',
          'version' => site.config['maintain_branch'],
          'jira_version' => site.config['maintain_branch'],
          'branch_name' => site.config['stable_branch'],
          'docs' => 'stable',
          'branch' => site.config['maintain_branch'],
          'series' => site.config['maintain_branch'][0..-3],
      }
      site.pages << dev

    end
  end

  # Subclass of `Jekyll::Page` with custom method definitions.
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
end