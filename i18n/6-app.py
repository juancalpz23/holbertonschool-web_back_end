#!/usr/bin/env python3
"""
Basic Flask app with Babel for locale support and user-based preferences
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Mock database of users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configuration class for Babel object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user(id):
    """
    Retrieve a user from the mock database.
    """
    if id and int(id) in users:
        return users[int(id)]
    return None


@app.before_request
def before_request():
    """
    Set the user object in Flask's global context
    before each request.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages
    based on priority order
    """
    # 1. Check for locale in URL parameter
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    # 2. Check for locale in user settings if user is logged in
    if g.get('user') and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user["locale"]

    # 3. Check the 'Accept-Language' header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():

    """Render the main page with a greeting based on login status."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
