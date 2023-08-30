#!/usr/bin/env python3
"""Simple flask app to practice i18n"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """Class to configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets the user parameter passed through the url"""
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """Gets the global user, works like flask session"""
    g.user = get_user()


@app.route('/')
def index():
    """Renders a simple webpage"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
