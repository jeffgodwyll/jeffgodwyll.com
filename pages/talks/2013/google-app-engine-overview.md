title: DevCongress - Google App Engine Overview and Demo
date: 2013-08-21
published: true

Slide presentation, demo and video of my talk about getting started on Google 
App Engine.

## Presentation

<iframe src="https://docs.google.com/presentation/d/16zQHq61ShMtUHP3KJMKamfnHTdI9By7JVE5hpuYJH-8/embed?start=false&loop=false&delayms=3000" frameborder="0" width="640" height="389" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Code for demo

Reposting from https://gist.github.com/jeffgodwyll/6300282.

`app.yaml`

    # The Configuration File

    application: your_app_id
    version: 1
    runtime: python27
    api_version: 1
    threadsafe: true

    handlers:
    - url: /favicon\.ico
      static_files: favicon.ico
      upload: favicon\.ico

    - url: .*
      script: main.app

    libraries:
    - name: webapp2
      version: "2.5.1"

`main.py`

    # The main.py file is our controller where the core application logic goes
 
    import webapp2
 
    class MainHandler(webapp2.RequestHandler):
        def get(self):
            self.response.write('Hello world!')
 
    app = webapp2.WSGIApplication([('/', MainHandler)],
                                  debug=True)


## Video

<blockquote class="twitter-tweet" lang="en"><p>Google AppEngine by Jeffrey Godwyll: <a href="http://t.co/ALmCk6u9B6">http://t.co/ALmCk6u9B6</a> via <a href="https://twitter.com/YouTube">@YouTube</a></p>&mdash; DevCongress (@DevCongress) <a href="https://twitter.com/DevCongress/status/443903694716018688">March 13, 2014</a></blockquote>
