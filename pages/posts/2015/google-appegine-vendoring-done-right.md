title: Google App Engine Vendoring Done Right
date: 2015-06-28
published: true
tags: [app engine, pip, python]

This is my personal approach to using pure third-party python packages
on [Google App Engine][gae].

[Installing pure third-party python libs][gae-third-party] in GAE is very well
documented.

With a little tweak you should even have zero issues working in a
[virtualenv][virtualenv], the modern and right way to work with python web
applications. Virtualenvs create an isolated Python environment
ensuring that application specific packages are isolated from system packages.

This approach(the one outlined in the docs) is quite easy and better.
But occasionally I just want to be able to quickly test some functionality from my python console and be sure too that this will work in my GAE dev environment. Some prefer to use
[GAE's interactive console][gae-console]. I do too at times, but nothing beats cool
[terminal colors][term-colors] and stuff :D.


### How I Vendor

One common path people follow is to install packages twice. One in their custom
`lib` folder for the development server and another in their virtual environment
. But I find it simpler to [symlink][symlink] the virtual environment's site
packages to my third-party folder named `lib`. The concept is simple in that we
essentially make our application's dependencies available in this folder and
with a little vendoring [awesomeness][1] (or [hell][2] depending on whichever
way you want to look at it) in the configuration of our GAE project, we're able
to use these dependencies locally, in dev and in production. For what it's
worth, I think it's awesome.

To vendor like I do follow these:

1. Go into your project's root

1. Create virtualenv with a desired name and activate it. I use `env`.

        $ virtualenv env
        $ source env/bin/activate

1. Symlink the virtualenv's site packages to the `lib` folder

        $ ln -s env/lib/python2.7/site-packages lib
   After, you should have a top level structure resembling something like this:

        .
        ├── appengine_config.py
        ├── app.yaml
        ├── env
        ├── lib -> env/lib/python2.7/site-packages
        ├── main.py
        └── requirements.txt

2. pip install your packages. They get auto added into the `lib` folder as well
   For example to install Flask you can just use:

        $ pip install flask

      This works well with a [requirement's file][pip-req]:

        $ pip install -r requirements.txt

      Even better this allows you to move about with your requirements file that I'm
sure you've come to love and just can't live without.


3. Edit or create `appengine_config.py` to enable vendoring

        from google.appengine.ext import vendor

        # Add any libraries installed in the "lib" folder.
        vendor.add('lib')

4. In the skip files section of your `app.yaml` be sure to skip the upload of
   your  virtual environment as shown on the last line in the following example

        skip_files:
        - ^(.*/)?#.*#$
        - ^(.*/)?.*~$
        - ^(.*/)?.*\.py[co]$
        - ^(.*/)?.*/RCS/.*$
        - ^(.*/)?\..*$
        - ^env$ #virtual environment's folder

Once the packages are properly set up for App Engine to access, you can just
fire up a python shell in your virtualenv to test stuff out. We can thus be
pretty certain that any nifty stuff we try in the virtualenv will be the same
thing we can put in our application's logic and expect the same results.


[gae]: https://cloud.google.com/appengine/
[1]: http://blog.jonparrott.com/managing-vendored-packages-on-app-engine/
[2]: https://gist.github.com/datagrok/8577287
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[gae-third-party]: https://cloud.google.com/appengine/docs/python/tools/libraries27
[gae-console]: https://cloud.google.com/appengine/docs/python/tools/devserver#Python_The_Interactive_Console
[pip-req]: https://pip.pypa.io/en/latest/user_guide.html#requirements-files
[symlink]: https://en.wikipedia.org/wiki/Symbolic_link
[term-colors]: https://github.com/jeffgodwyll/dotfiles/blob/master/.config/terminator/config#L29
