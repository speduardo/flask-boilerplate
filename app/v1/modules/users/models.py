from app.v1.core.api import api_v1
from flask_restplus import fields


class UserModel:

    model = api_v1.model('User', {
        'id': fields.Integer(description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(attribute='password_hash', required=True, description='user password')
    })

    model_parameter = api_v1.model('User', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(attribute='password_hash', required=True, description='user password')
    })
