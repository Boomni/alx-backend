#!/usr/bin/env python3
"""Simple flask app to practice i18n"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config():
    """Class to configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    """Renders a simple webpage"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """Get locale from request"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
