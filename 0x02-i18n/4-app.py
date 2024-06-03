#!/usr/bin/env python3
"""implement a way to force a particular locale by
    passing the locale=fr parameter to your app’s URLs."""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_local() -> str:
    """ Determine the best match
        with supported languages
    """
    langopt = request.args.get('locale')
    if langopt and langopt in app.config['LANGUAGES']:
        return langopt

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The '/' path to the index.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
