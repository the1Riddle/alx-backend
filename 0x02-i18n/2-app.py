#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuring available languages
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    display index.html file from the templates folder
    and has Welcome to Holberton title
    """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """
    get locale from request
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
