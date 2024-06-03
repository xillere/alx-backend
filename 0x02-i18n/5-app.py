#!/usr/bin/env python3
"""implement a way to force a particular locale by
    passing the locale=fr parameter to your app’s URLs."""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """ returns a user dictionary or None
        if the ID cannot be found or if
        login_as was not passed.
    """
    loginid = request.args.get('login_as')
    if loginid is None:
        return None
    return users.get(int(loginid))


@app.before_request
def before_request() -> None:
    """to find a user if any, and set
        it as a global on flask.g.user
    """
    g.user = get_user()

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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
