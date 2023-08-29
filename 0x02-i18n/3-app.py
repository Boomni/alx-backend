#!/usr/bin/env python3
"""Simple flask app to practice i18n"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)


class Config():
    """Class to configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """Renders a simple webpage"""
    home_title: str = _('Welcome to Holberton')
    home_header: str = _('Hello world!')
    return render_template(
            "3-index.html",
            home_title=home_title,
            home_header=home_header
            )


@babel.localeselector
def get_locale():
    """Get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()