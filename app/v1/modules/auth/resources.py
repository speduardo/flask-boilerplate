from flask import current_app, request
from flask_restplus import Resource, Namespace, fields
from app.v1.modules.users.dto import User
from app.v1.modules.users.models import UserModel
from app.v1.modules.auth.models import RefreshToken
from app.v1.extensions import db
from app.v1.extensions.api import api_v1
from app.v1.exceptions import ValidationException
import re
import jwt
import datetime
import hashlib

api = Namespace('auth', description="Authentication")
register_model = api_v1.model('Register', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

token_model = api_v1.model('ReturnToken', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True)
})


@api.route('/register')
class Register(Resource):
    # 4-16 symbols, can contain A-Z, a-z, 0-9, _ (_ can not be at the begin/end and can not go in a row (__))
    USERNAME_REGEXP = r'^(?![_])(?!.*[_]{2})[a-zA-Z0-9._]+(?<![_])$'

    # 6-64 symbols, required upper and lower case letters. Can contain !@#$%_  .
    PASSWORD_REGEXP = r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d!@#$%_]{6,64}$'

    @api.expect(register_model, validate=True)
    @api.marshal_with(UserModel.model)
    @api.response(400, 'username or password incorrect')
    def post(self):
        if not re.search(self.USERNAME_REGEXP, api_v1.payload['username']):
            raise ValidationException(error_field_name='username',
                                      message='4-16 symbols, can contain A-Z, a-z, 0-9, _ \
                                      (_ can not be at the begin/end and can not go in a row (__))')

        if not re.search(self.PASSWORD_REGEXP, api_v1.payload['password']):
            raise ValidationException(error_field_name='password',
                                      message='6-64 symbols, required upper and lower case letters. Can contain !@#$%_')

        if User.query.filter_by(username=api_v1.payload['username']).first():
            raise ValidationException(error_field_name='username', message='This username is already exists')

        user = User(username=api_v1.payload['username'], password=api_v1.payload['password'])
        db.session.add(user)
        db.session.commit()
        return user


@api.route('/login')
class Login(Resource):
    @api.expect(register_model)
    @api.response(200, 'Success', token_model)
    @api.response(401, 'Incorrect username or password')
    def post(self):
        """
        Look implementation notes
        This API implemented JWT. Token's payload contain:
        'uid' (user id),
        'exp' (expiration date of the token),
        'iat' (the time the token is generated)
        """
        user = User.query.filter_by(username=api_v1.payload['username']).first()
        if not user:
            api.abort(401, 'Incorrect username or password')

        from werkzeug.security import check_password_hash
        if check_password_hash(user.password_hash, api_v1.payload['password']):
            _access_token = jwt.encode({'uid': user.id,
                                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
                                        'iat': datetime.datetime.utcnow()},
                                       current_app.config['SECRET_KEY']).decode('utf-8')
            _refresh_token = jwt.encode({'uid': user.id,
                                         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                                         'iat': datetime.datetime.utcnow()},
                                        current_app.config['SECRET_KEY']).decode('utf-8')

            user_agent_string = request.user_agent.string.encode('utf-8')
            user_agent_hash = hashlib.md5(user_agent_string).hexdigest()

            refresh_token = RefreshToken.query.filter_by(user_agent_hash=user_agent_hash).first()

            if not refresh_token:
                refresh_token = RefreshToken(user_id=user.id, refresh_token=_refresh_token,
                                             user_agent_hash=user_agent_hash)
            else:
                refresh_token.refresh_token = _refresh_token

            db.session.add(refresh_token)
            db.session.commit()
            return {'access_token': _access_token, 'refresh_token': _refresh_token}, 200

        api.abort(401, 'Incorrect username or password')


@api.route('/refresh')
class Refresh(Resource):
    @api.expect(api_v1.model('RefreshToken', {'refresh_token': fields.String(required=True)}), validate=True)
    @api.response(200, 'Success', token_model)
    def post(self):
        _refresh_token = api_v1.payload['refresh_token']

        try:
            payload = jwt.decode(_refresh_token, current_app.config['SECRET_KEY'])

            refresh_token = RefreshToken.query.filter_by(user_id=payload['uid'], refresh_token=_refresh_token).first()

            if not refresh_token:
                raise jwt.InvalidIssuerError

            # Generate new pair

            _access_token = jwt.encode({'uid': refresh_token.user_id,
                                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
                                        'iat': datetime.datetime.utcnow()},
                                       current_app.config['SECRET_KEY']).decode('utf-8')
            _refresh_token = jwt.encode({'uid': refresh_token.user_id,
                                         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                                         'iat': datetime.datetime.utcnow()},
                                        current_app.config['SECRET_KEY']).decode('utf-8')

            refresh_token.refresh_token = _refresh_token
            db.session.add(refresh_token)
            db.session.commit()

            return {'access_token': _access_token, 'refresh_token': _refresh_token}, 200

        except jwt.ExpiredSignatureError as e:
            raise e
        except (jwt.DecodeError, jwt.InvalidTokenError)as e:
            raise e
        except:
            api.abort(401, 'Unknown token error')


from app.v1.utils import token_required


# This resource only for test
@api.route('/protected')
class Protected(Resource):
    @token_required
    def get(self, current_user):
        return {'i am': 'protected', 'uid': current_user.id}
