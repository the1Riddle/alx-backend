#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    display index.html file from the templates folder
    and has Welcome to Holberton title
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
