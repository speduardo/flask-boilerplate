import uuid
import datetime
from flask import json
from enum import EnumMeta
from flask_sqlalchemy.model import Model
from app.v1.core import db


class BaseDAO(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def create(cls, data):
        db.session.add(data)
        db.session.commit()
        db.session.flush()

        return data

    @classmethod
    def update(cls, entity):
        db.session.merge(entity)
        db.session.commit()

        return entity

    @classmethod
    def delete(cls, id):
        entity = cls.query.get(id)
        db.session.delete(entity)
        db.session.commit()

        return entity

    @classmethod
    def rollback(cls):
        db.session.rollback()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def find_by_name(cls, filtro):
        return cls.query.filter(cls.name.like(filtro)).first()
        # return cls.query.filter(cls[propriedade].like(filtro)).first()
