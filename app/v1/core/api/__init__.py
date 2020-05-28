"""
API extension
=============
"""

from copy import deepcopy

from flask import current_app

from flask_restplus import Api
# from .api import Api
# from .namespace import Namespace
# from .http_exceptions import abort


api_v1 = Api( # pylint: disable=invalid-name
    version='1.0',
    title="Flask-Boilerplate Example API",
    description=(
        "It is a [real-life example RESTful API server implementation using Flask-RESTplus]"
        "(https://github.com/leonhardt/flask-boilerplate).\n\n"
    ),
)


def serve_swaggerui_assets(path):
    """
    Swagger-UI assets serving route.
    """
    if not current_app.debug:
        import warnings
        warnings.warn(
            "/swaggerui/ is recommended to be served by public-facing server (e.g. NGINX)"
        )
    from flask import send_from_directory
    return send_from_directory('../static/', path)


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    API extension initialization point.
    """
    #app.route('/swaggerui/<path:path>')(serve_swaggerui_assets)

    # Prevent config variable modification with runtime changes
    #api_v1.authorizations = deepcopy(app.config['AUTHORIZATIONS'])

#@api_v1.errorhandler(ValidationException)
#def handle_validation_exception(error):
#    return {'message': 'Validation error', 'errors': {error.error_field_name: error.message}}, 400


#@api_v1.errorhandler(jwt.ExpiredSignatureError)
#def handle_expired_signature_error(error):
#    return {'message': 'Token expired'}, 401


#@api_v1.errorhandler(jwt.InvalidTokenError)
#@v1_api.errorhandler(jwt.DecodeError)
#@v1_api.errorhandler(jwt.InvalidIssuerError)
#def handle_invalid_token_error(error):
#    return {'message': 'Token incorrect, supplied or malformed'}, 401
