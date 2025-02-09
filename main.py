import locale
import os
import re
import subprocess
import argh
import yaml

from collections import OrderedDict
from datetime import date, datetime
from flask import Flask, render_template, abort, send_from_directory
from flask_frozen import Freezer
from flask_flatpages import FlatPages

from flaskext.markdown import Markdown
from unicodedata import category, normalize

import assets

# Configuration
if os.environ.get("SERVER_SOFTWARE", "").startswith("Development"):
    DEBUG = True
else:
    DEBUG = False

BASE_URL = "http://jeffgodwyll.com"
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = ".md"
FLATPAGES_ROOT = "pages"

# App configuration
FEED_MAX_LINKS = 25
SECTION_MAX_LINKS = 12

app = Flask(__name__)
app.config.from_object(__name__)
assets.init(app)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(
    app,
    extensions=["fenced_code"],
    output_format="html5",
)

# social profiles
with open("./social.yaml", "r") as f:
    profiles = yaml.safe_load(f)

SOCIAL_PROFILES = OrderedDict(sorted(profiles.items()))


###############################################################################
# Model helpers


def get_pages(pages, offset=None, limit=None, section=None, year=None):
    """Retrieves pages matching passed criterias."""
    articles = list(pages)
    # assign section value if none was provided in the metas
    for article in articles:
        if not article.meta.get("section"):
            article.meta["section"] = article.path.split("/")[0]
    # filter unpublished article
    if not app.debug:
        articles = [p for p in articles if p.meta.get("published") is True]
    # filter section
    if section:
        articles = [p for p in articles if p.meta.get("section") == section]
    # filter year
    if year:
        articles = [p for p in articles if p.meta.get("date").year == year]
    # sort by date
    articles = sorted(
        articles, reverse=True, key=lambda p: p.meta.get("date", date.today())
    )
    # assign prev/next page in serie
    for i, article in enumerate(articles):
        if i != 0:
            if section and articles[i - 1].meta.get("section") == section:
                article.prev = articles[i - 1]
        if i != len(articles) - 1:
            if section and articles[i + 1].meta.get("section") == section:
                article.next = articles[i + 1]
    # offset and limit
    if offset and limit:
        return articles[offset:limit]
    elif limit:
        return articles[:limit]
    elif offset:
        return articles[offset:]
    else:
        return articles


def get_years(pages):
    years = list(set([page.meta.get("date").year for page in pages]))
    years.reverse()
    return years


def section_exists(section):
    return not len(get_pages(pages, section=section)) == 0


def slugify(text, delim="-"):
    """Generates an slightly worse ASCII-only slug."""
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize("NFKD", word).encode("ascii", "ignore")
        if word:
            result.append(word)
    return str(delim.join(word.decode("ascii") for word in result))


###############################################################################
# Filters


@app.template_filter()
def to_rfc2822(dt):
    if not dt:
        return
    current_locale = locale.getlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_TIME, "en_US")
    formatted = dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
    locale.setlocale(locale.LC_TIME, current_locale)
    return formatted


@app.template_filter()
def read_time(text, words_per_min=250):
    """Estimate reading time, medium-style"""
    # remove punctuations
    text = "".join(
        character for character in text if not category(character).startswith("P")
    )
    num_words = len(text.split())
    # round to nearest whole number
    average_time = (num_words + words_per_min // 2) // words_per_min
    return 1 if average_time == 0 else average_time


###############################################################################
# Context processors


@app.context_processor
def inject_ga():
    return dict(BASE_URL=BASE_URL)


###############################################################################
# Routes


@app.route("/about/")
def about():
    return render_template("about.html", accounts=SOCIAL_PROFILES)


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/")
def index():
    return render_template(
        "index.html",
        posts=get_pages(pages, limit=5, section="posts"),
        talks=get_pages(pages, limit=5, section="talks"),
    )


@app.route("/<path:path>/")
def page(path):
    # compute current "section" from path
    section = path.split("/")[0]
    page = pages.get_or_404(path)
    # ensure an accurate "section" meta is available
    page.meta["section"] = page.meta.get("section", section)
    # allow preview of unpublished stuff in DEBUG mode
    if not app.debug and not page.meta.get("published", False):
        abort(404)
    template = page.meta.get("template", "%s/page.html" % section)
    return render_template(template, page=page, section=section)


@app.route("/<string:section>/")
def section(section):
    if not section_exists(section):
        abort(404)
    template = "%s/index.html" % section
    articles = get_pages(pages, limit=SECTION_MAX_LINKS, section=section)
    years = get_years(get_pages(pages, section=section))
    return render_template(template, pages=articles, years=years)


@app.route("/<string:section>/<int:year>/")
def section_archives_year(section, year):
    if not section_exists(section):
        abort(404)
    template = "%s/archives.html" % section
    years = get_years(get_pages(pages, section=section))
    articles = get_pages(pages, section=section, year=year)
    return render_template(template, pages=articles, years=years, year=year)


@app.route("/tag/<string:tag>/")
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    return render_template("tag/archives.html", pages=tagged, tag=tag)


@app.route("/.well-known/acme-challenge/<path:path>")
def acme_challenge(path):
    return send_from_directory("static/acme-challenge", path, mimetype="text/plain")


@app.route("/403.html")
def error403():
    return render_template("403.html")


@app.route("/404.html")
def error404():
    return render_template("404.html")


@app.route("/500.html")
def error500():
    return render_template("500.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


###############################################################################
# Commands
def build():
    """Build sitemap and feeds locally before putting on GAE"""

    @app.route("/feed.xml")
    def feed():
        articles = get_pages(pages, limit=FEED_MAX_LINKS)
        now = datetime.now()
        return render_template("base.xml", pages=articles, build_date=now)

    @app.route("/sitemap.xml")
    def sitemap():
        today = date.today()
        recently = date(year=today.year, month=today.month, day=1)
        return render_template(
            "sitemap.xml", pages=get_pages(pages), today=today, recently=recently
        )

    app.debug = False
    freezer.freeze()
    print("Regenerating feeds and sitemap...")

    subprocess.call("cp ./build/*.xml ./static/", shell=True)
    print("Cleaning up...")
    subprocess.call("rm -rf ./build/", shell=True)

    print("Bundling and minifying js and css files...")
    assets.build()
    print("Done!")


def run():
    app.run(debug=True)


if __name__ == "__main__":
    parser = argh.ArghParser()
    parser.add_commands([build, run])
    parser.dispatch()
