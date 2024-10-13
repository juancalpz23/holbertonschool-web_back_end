#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Import and initialize authentication class based on AUTH_TYPE
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """
    Handler for filtering each request before it is processed.
    """
    if auth is None:
        return  # Do nothing if no authentication instance is available

    # List of paths that don't require authentication
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]

    # Check if the request requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        return  # Do nothing if the request path is excluded

    # Validate the Authorization header
    if auth.authorization_header(request) is None:
        abort(401)  # Raise 401 Unauthorized if header is missing

    # Assign the current user to the request
    request.current_user = auth.current_user(request)

    # Validate the current user
    if request.current_user is None:
        abort(403)  # Raise 403 Forbidden if user is not authenticated


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
