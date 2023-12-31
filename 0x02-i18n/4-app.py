#!/usr/bin/env python3

"""Flask app"""

from flask import Flask, render_template, request, session
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class Config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with the supported languages"""
    force_locale = request.args.get('locale')

    if force_locale and force_locale in app.config['LANGUAGES']:
        return force_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """index method"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
