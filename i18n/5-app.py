#!/usr/bin/env python3
"""Basic Flask app with Babel and mock login"""

from flask import Flask, g, render_template, request
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
babel = Babel(app)


def get_user(user_id):
    """Retrieve a user by ID from the users dictionary."""
    try:
        return users.get(int(user_id))
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Executed before each request, setting g.user if available."""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello():
    """Render the template with translatable strings and user info."""
    login = g.get('user') is not None
    return render_template('5-index.html', login=login)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    if g.get('user') and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
