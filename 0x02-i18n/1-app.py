#!/usr/bin/env python3
"""Simple flask app to practice i18n"""
from flask import Flask, render_template
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
def index():
    """Renders a simple webpage"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
