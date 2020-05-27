from marshmallow import fields
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import ModelConverter, SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field, property2field
from werkzeug.security import generate_password_hash
from app.v1.extensions.api import api_v1
from app.v1.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(250))
    email = db.Column(db.String(length=120), unique=True, nullable=False)

    #first_name = db.Column(db.String(length=30), default='', nullable=False)
    #middle_name = db.Column(db.String(length=30), default='', nullable=False)
    #last_name = db.Column(db.String(length=30), default='', nullable=False)

    from ..auth.models import RefreshToken
    #refresh_tokens = relationship('RefreshToken', backref='user')
    from ..todos.models import Todo
    #todos = relationship('Todo', backref='user')

    @property
    def password(self):
        raise AttributeError('Password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("password_hash",)

        include_relationships = True
        load_instance = True
        transient = True

    password = fields.Inferred()
