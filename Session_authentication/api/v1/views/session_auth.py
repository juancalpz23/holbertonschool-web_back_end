#!/usr/bin/env python3
"""
Module of Session Authentication views
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
from api.v1.app import auth  # Import here to avoid circular import
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
@app_views.route('/auth_session/login/',
                 methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /api/v1/auth_session/login
    Return:
      - JSON representation of the User object if successful
      - 400 if email or password is missing
      - 404 if no user found for the email
      - 401 if the password is wrong
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search(email)  # Find the User by email
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session for the user
    session_id = auth.create_session(user.id)  # Create session ID
    response = jsonify(user.to_json())  # Get the User JSON representation
    response.set_cookie(getenv("SESSION_NAME", "_my_session_id"), session_id)
    return response
