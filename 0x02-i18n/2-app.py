#!/usr/bin/env python3

"""Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class Config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """Determines the best match with the supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index method"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
