from flask_bcrypt import generate_password_hash
from app.v1.core import db
from app.v1.core.daos import BaseDAO


class UserDAO(BaseDAO):
    __tablename__ = 'user'

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
        self.password_hash = generate_password_hash(password).decode('utf-8')
