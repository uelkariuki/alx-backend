#!/usr/bin/env python3

"""Flask app"""

from typing import Dict
from flask import Flask, render_template, request, session, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class Config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """Determines the best match with the supported languages"""
    force_locale = request.args.get('locale')

    if force_locale and force_locale in app.config['LANGUAGES']:
        return force_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id) -> Dict:
    """get user method"""
    if user_id in users:
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any, and set it as a global on flask.g.user
    """

    user_id = request.args.get('login_as')
    g.user = None
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """index method"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
