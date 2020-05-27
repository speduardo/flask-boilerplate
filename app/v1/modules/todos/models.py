from flask_restplus import fields
from sqlalchemy import ForeignKey
from app.v1.extensions import db
from app.v1.extensions.api import api_v1


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    task = db.Column(db.String(50))
    done = db.Column(db.Boolean(), default=False)

    todo_resource_model = api_v1.model('Todo', {
        'id': fields.Integer(readOnly=True, description='The task unique identifier. ReadOnly.'),
        'task': fields.String(required=True, description='The task details'),
        'done': fields.Boolean(description='Bla bla bla')
    })
