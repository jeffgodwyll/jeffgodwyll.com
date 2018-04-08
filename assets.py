from flask import Flask
from flask_assets import Bundle, Environment


def init(app=None):
    app = app or Flask(__name__)
    with app.app_context():
        assets = Environment(app)
        assets.auto_build = False
        assets.manifest = 'file:./manifest'

        css = Bundle(
            'css/style.css',
            'js/libs/prettify/*.css',
            filters='cssmin', output='css/styles.min.css',
        )
        assets.register('css', css)

        js = Bundle(
            'js/app.js',
            'js/libs/prettify/*.js',
            'js/libs/jquery-1.7.1.min.js',
            filters='jsmin', output='js/main.min.js'
        )
        assets.register('js', js)

        bundles = [css, js]
        return bundles


def build():
    bundles = init()
    for bundle in bundles:
        bundle.build()


if __name__ == '__main__':
    build()
