title: Let's Encrypt Google App Engine
date: 2016-01-02
published: true
tags: [python, flask, app engine]

> Let’s Encrypt is a free, automated,
> and open certificate authority (CA), run for the public’s benefit. Let’s Encrypt
> is a service provided by the Internet Security Research Group (ISRG)

> [About, Let's Encrypt][letsencrypt_about]

This post won't go into details as to what Let's Encrypt is about. We should
probably read the [FAQ's][letsencrypt_faq] if we want to learn more.

Until the Google App Engine Team fully automate the process of using Let's
Encrypt on Google App Engine or even provide some sort of API to handle certs,
we'll probably have to find ways of either automating the process just a little
bit or stick to some other easier cert authority. You can track work on this in
[Issue 12535][gae_issue]. There's a catch.

But come on who doesn't like free, open, "secure" stuff? I know I do.

So to get started, we'll follow the instructions [here][letsencrypt_client_inst]
to install the [Let's Encrypt Client][letsencrypt_client]

> The Let's Encrypt Client is a fully-featured, extensible client for the Let's
> Encrypt CA (or any other CA that speaks the ACME protocol) that can automate
> the tasks of obtaining certificates and configuring webservers to use them.

Next is to obtain a certificate using the manual plugin like so:

    $ sudo ./letsencrypt-auto -a manual certonly

We'll be prompted for a couple of things, like the domain names we're
generating the cert(s) for, and  getting our IP logged.

Last but not least, we'll be presented with a challenge, the most crucial
part, where we'll be presented with something like this at the let's encrypt
console:

<pre class="prettyprint nocode " style="font-size: 75%">
Make sure our web server displays the following content at
http://www.example.com/.well-known/acme-challenge/odebEMaSagM3xRblm_hmcPvnpCFdEsTBDrpaHyw6Q_I
before continuing:

odebEMaSagM3xRblm_hmcPvnpCFdEsTBDrpaHyw6Q_I.du6Wm_JOQBK08bH0MzKjuVzNbozezAthZBONRGcghDI
...
...
Press <kbd>ENTER</kbd> to continue
</pre>

This is fairly straightforward. We can choose to serve the challenge text and
content from a special directory within our app and ensure they match
correspondingly.


For example in our GAE project directory, we could do the following:

    $ mkdir -p well-known/acme-challenge/

    $ echo "odebEMaSagM3xRblm_hmcPvnpCFdEsTBDrpaHyw6Q_I.du6Wm_JOQBK08bH0MzKjuVzNbozezAthZBONRGcghDI" > well-known/acme-challenge/odebEMaSagM3xRblm_hmcPvnpCFdEsTBDrpaHyw6Q_I


And then the challenge can be handled in a number of ways, like for my flask GAE
apps, I prefer to create a simple flask route to help with current and future
challenges

    from flask import Flask, send_from_directory

    app = Flask(__name__)

    @app.route('/.well-known/acme-challenge/<path:path>')
    def acme_challenge(path):
        return send_from_directory('well-known/acme-challenge',
                                   path, mimetype='text/plain')

This means the challenges will be stored in a directory structure similar to:

    .
    ├── app.yaml
    ├── main.py
    └── well-known
        └── acme-challenge
                └── odebEMaSagM3xRblm_hmcPvnpCFdEsTBDrpaHyw6Q_I


If we happen to be using a different runtime, running a static site on GAE or we
just love using `yaml`, we can as well handle this in our `app.yaml`:

    handlers:
    - url: /.well-known/acme-challenge/(.*)
      mime_type: text/plain
      static_files: well-known/acme-challenge/\1
      upload: well-known/acme-challenge/.*

Upload all changes to our live environment and test that we can reach the
endpoint:

    $ appcfg.py update .

Head back to our Let's Encrypt console, hit <kbd>enter</kbd> to verify the
challenge and get the certs generated.

If successful, the certificates will then reside in `/etc/letsencrypt/live/<path_to_site>`

We'll then convert our `privkey.pem` into an [RSA][rsa] private key for use in the
[Google Cloud Developers Console][gcloud_ssl_section]:

    $ opennssl rsa -in privkey.pem -out rsa.pem

First, copy `fullchain.pem` into the
[Google Cloud Developers Console SSL Certificates Section][gcloud_ssl_section]:

    $ xclip -sel clip < fullcain.pem

Same for `rsa.pem`:

    $ xclip -sel clip < rsa.pem

![Google Cloud Dev Console][google_cloud_console_cert]


Enable `https` and voilà!

Okay, not exactly done because if you took note from the very beginning I said
that's there's a catch :D. You'll have to remember to repeat parts of  this every 3 months to
ensure you enjoy continue to enjoy this.

Let's star [GAE Issue 12535][gae_issue]. Maybe the more
the interest, the faster this is worked on.

Enjoy!

[letsencrypt_about]: https://letsencrypt.org/about/
[letsencrypt_client]: https://github.com/letsencrypt/letsencrypt/
[letsencrypt_client_inst]: https://github.com/letsencrypt/letsencrypt/#installation
[letsencrypt_faq]: https://community.letsencrypt.org/c/docs/
[google_cloud_console_cert]: https://lh3.googleusercontent.com/qPqpny-bowhMhKjB-eM43wOwR_siBIwASlr0qVoCsE8EUWklbXEdtty7IpFDIlm3dHzYr9LjDGZF=w1359-h641-no
[gae_issue]: https://code.google.com/p/googleappengine/issues/detail?id=12535
[rsa]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[gcloud_ssl_section]: https://console.developers.google.com/appengine/settings/certificates
