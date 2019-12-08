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

    Defaults to returning hotels at specific location.

    Location is determined by 'at' query parameter, however, if not provided \
        this endpoint makes suitable guess based on client's IP address and \
        location information obtained from IP Stack API.

    """

    if not app.config["HERE_APP_ID"] or not app.config["HERE_APP_CODE"]:
        raise InvalidUsage("Here Places API settings are missing. Please consult README.", \
            status_code=400)


    query = request.args.get("q", default="hotels")
    at = request.args.get("at", default=None)

    # If lat, long is not provided, get it based on Client IP
    if not at:
        at = get_lat_long(request)

    config = app.config
    payload = {
        "at": at,
        "q": query,
        "app_id": config["HERE_APP_ID"],
        "app_code": config["HERE_APP_CODE"]
    }
    
    here_api_url = config["HERE_API_URL"]

    response = requests.get(here_api_url, payload)
    return response.json(), 200


def get_lat_long(request):
    """
    Gets the best possible client IP address,
    either from X-Forwarded-For or remote address set in request object.

    Based on IP found, gets latitude and longitude from IP Stack API.
    
    Arguments:
        request {[flask.request]} -- Current request object.
    
    Returns:
        [String] -- Comma separated latitude.longitude.
    """

    remote_addr, lat_long = None, None

    # Are we behind a proxy?
    if 'X-Forwarded-For' in request.headers:
        remote_addr = request.headers['X-Forwarded-For']
    else:
        remote_addr = request.remote_addr

    # Are we testing locally? Return a suitable default.
    if remote_addr == '127.0.0.1' or not app.config["IPSTACK_API_KEY"]:
        return "40.74917,-73.98529"

    ipstack_api_key = app.config["IPSTACK_API_KEY"]
    ipstack_api_url = app.config["IPSTACK_URL"] + remote_addr + \
                        '?' + "access_key=" + ipstack_api_key
    ips_response = requests.get(ipstack_api_url)
    if ips_response.status_code == 200:
        ips_data = ips_response.json()
        if str(ips_data["latitude"]) == "None" or str(ips_data["longitude"]) == "None":
            return "40.74917,-73.98529"
        lat_long = str(ips_data["latitude"]) + "," + str(ips_data["longitude"])

    return lat_long


# Catch all other requests and return suitable status code with message
@app.route('/', defaults={'path': ''}, methods=['POST', 'PUT', 'PATCH', 'GET'])
@app.route('/<path:path>')
def catch_all(path):
    raise InvalidUsage('Method Not Allowed', status_code=405)

