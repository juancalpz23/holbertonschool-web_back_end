#!/usr/bin/env python3
"""Flask app with mock user login and welcome message"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Determine the best match with supported languages."""
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


def get_user():
    """Retrieve a user by ID from the URL parameter login_as."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Executed before each request, setting g.user if available."""
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """Render the template with translatable strings and user info"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
