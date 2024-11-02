#!/usr/bin/env python3
"""Flask app with template parameterization for translations"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Determine the best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """Render the template with translatable strings"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
