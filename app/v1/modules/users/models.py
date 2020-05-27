from flask_restplus import fields
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from werkzeug.security import generate_password_hash
from app.v1.extensions.api import api_v1
from app.v1.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(80))
    email = db.Column(db.String(length=120), unique=True, nullable=False)

    first_name = db.Column(db.String(length=30), default='', nullable=False)
    middle_name = db.Column(db.String(length=30), default='', nullable=False)
    last_name = db.Column(db.String(length=30), default='', nullable=False)

    from ..auth.models import RefreshToken
    refresh_tokens = relationship('RefreshToken', backref='user')
    from ..todos.models import Todo
    todos = relationship('Todo', backref='user')

#    @property
#    def password(self):
#        raise AttributeError('Password not readable')

#    @password.setter
#    def password(self, password):
#        self.password_hash = generate_password_hash(password)

    user_resource_model = api_v1.model('User', {
        'username': fields.String(required=True)
    })


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
