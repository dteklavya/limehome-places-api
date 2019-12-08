from flask import jsonify, request
from flask import current_app as app
import requests

from application.exceptions import InvalidUsage


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    '''
        All route and query related exceptions lang up in this sink.
    '''
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/places', methods=['GET'])
def get_root():
    """
    Returns results from Here Places API as is returned.

    """

    if not app.config["HERE_APP_ID"] or not app.config["HERE_APP_CODE"]:
        raise InvalidUsage("Here Places API settings are missing. Please consult README.", \
            status_code=400)

    return jsonify([]), 200
