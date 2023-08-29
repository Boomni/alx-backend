#!/usr/bin/env python3
"""Simple flask app to practice i18n"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Renders a simple webpage"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
