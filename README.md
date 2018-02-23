## jeffgodwyll.com

Source of [my personal homepage](https://jeffgodwyll.com).

Built on [Google App Engine](https://appengine.google.com) with the
[Flask micro framework](http://flask.pocoo.org) and some cool flask extensions 
too.

You can easily convert this into a static site builder if needed :)

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone https://github.com/jeffgodwyll/jeffgodwyll.com.git
   ```
3. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project 
   directory.

   ```
   cd jeffgodwyll.com
   pip install -r requirements.txt -t lib
   ```
4. Change the `BASE_URL` value to point to your address
5. Edit `app.yaml` with the appropriate app id
6. I prefer to build the sitemap and feeds locally before uploading them as 
  static files. You can dynamically generate it and write to the datastore or 
  Google cloud storage.
  If you prefer option 1 like I do, then run the following to build them in place.

    ```
    python main.py build
    ```

6. Run this project locally from the command line:

   ```
   dev_appserver.py .
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
*Please don't deploy this as is* It's my personal blog/site. 
See the [licensing](#Licensing)for more details.

**Important note again: You can't republish the blog with its contents as-is 
anywhere on the internet.
Personalise it as much as you can. Don't hesitate to use the issue tracker if 
you want something explained**

Now that that's out of the way, to deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
2. Edit `Makefile` and replace `PROJECT_ID` variable with your project id
3. [Deploy the application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   make deploy
   ```

   or

   ```
   gcloud app deploy --project <<YOUR_PROJECT_ID>>
   ```
4. Congratulations!  Your site is now live at your-app-id.appspot.com


### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Licensing
Contents in `./pages` (blog posts and talks) are Copyright of Jeffrey Godwyll.

All the rest including Python code, templates, CSS & javascript are licensed 
under the MIT License. You're free to use them and link back to 
https://github.com/jeffgodwyll/jeffgodwyll.com OR not :)

See: http://jeff.mit-license.org/
