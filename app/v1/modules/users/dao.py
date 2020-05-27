from app.v1.extensions import db


class UserDAO(object):
    __db = None

    def __init__(self):
        self.__db = db

    def get(self, id):
        return self.__db.query.get(id)

    def findAll(self):
        return self.__db.query("SELECT * FROM users", None).fetchall()

    def create(self, data):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass