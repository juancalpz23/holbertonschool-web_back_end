#!/usr/bin/env python3
"""
Index
"""


from flask import Blueprint, abort

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    """ Endpoint that raises a 401 error """
    abort(401)
