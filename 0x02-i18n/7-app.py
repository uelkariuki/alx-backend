#!/usr/bin/env python3

"""Flask app"""

from typing import Dict
from flask import Flask, render_template, request, session, g
from flask_babel import Babel
import pytz
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """class Config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with the supported languages"""

    # locale from url parameters
    force_locale = request.args.get('locale')

    if force_locale and force_locale in app.config['LANGUAGES']:
        return force_locale

    # Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@babel.timezoneselector
def get_timezone():
    """Get timezone function"""
    try:

		# Timezone parameter in URL parameters
        url_timezone = request.args.get('timezone')
        if url_timezone:
             pytz.timezone(url_timezone)
             return url_timezone

		# time zone from user settings
        if g.user and g.user['timezone']:
             pytz.timezone(g.user['timezone'])
             return g.user['timezone']

    except UnknownTimeZoneError:
        pass

	# Default to UTC
    return 'UTC'


def get_user(id):
    """get user method"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """
    use get_user to find a user if any, and set it as a global on flask.g.user
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """index method"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(debug=True)
