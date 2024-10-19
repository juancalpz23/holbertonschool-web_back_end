#!/usr/bin/env python3
"""
Basic Flask app.
"""
from flask import Flask, jsonify, redirect, request, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """
    GET route that returns a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    POST /users route to register a new user.
    Expects 'email' and 'password' form data.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    POST /sessions route to log in a user.
    Expects 'email' and 'password' form data.
    If successful, creates a session and sets a cookie.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)  # Respond with 401 Unauthorized if credentials are invalid

    session_id = AUTH.create_session(email)  # Create session ID for the user
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    """
    DELETE /sessions route to log out a user.
    - Expects 'session_id' as a cookie.
    - If session exists, destroy it and redirect to GET /.
    - If no session is found, respond with a 403 HTTP status.
    """
    session_id = request.cookies.get("session_id")

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/", code=302)


@app.route("/profile", methods=["GET"])
def profile() -> str:
    """
    GET /profile route to retrieve the user's profile.
    Expects 'session_id' as a cookie.
    - If the user exists, return a 200 status with their email.
    - If the session is invalid or user does not exist, return 403.
    """
    session_id = request.cookies.get("session_id")

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """
    POST /reset_password route to generate a reset password token.
    Expects 'email' form data.
    """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
