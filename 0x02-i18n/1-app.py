#!/usr/bin/env python3


"""Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

class Config(object):
    """class Config"""

    LANGUAGES = ["en", "fr"]
    
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """set locale to english"""
    return 'en'

@babel.timezoneselector
def get_timezone():
    """Set timezone"""
    return 'UTC'

@app.route('/')
def index():
    """index method"""
    return render_template('0-index.html')





if __name__ == "__main__":
    app.run(debug=True)
