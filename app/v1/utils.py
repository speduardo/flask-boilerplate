import jwt
from flask import request, current_app
from app.v1.modules.users.daos import UserDAO
from .core.api import api_v1


# required_token decorator
def token_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        current_user = None
        if auth_header:
            try:
                access_token = auth_header.split(' ')[1]

                try:
                    token = jwt.decode(access_token, current_app.config['SECRET_KEY'])
                    current_user = UserDAO.query.get(token['uid'])
                except jwt.ExpiredSignatureError as e:
                    raise e
                except (jwt.DecodeError, jwt.InvalidTokenError) as e:
                    raise e
                except:
                    api_v1.abort(401, 'Unknown token error')

            except IndexError:
                raise jwt.InvalidTokenError
        else:
            api_v1.abort(403, 'Token required')
        return f(*args, **kwargs, current_user=current_user)

    wrapper.__doc__ = f.__doc__
    wrapper.__name__ = f.__name__
    return wrapper
