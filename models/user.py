import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    password = db.Column(db.String(20))
    email = db.Column(db.String(30))
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, username, password, email, first_name, last_name, is_active):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def update_from_db(cls, _username, new_data):
        audiodata = cls.query.filter_by(username=_username).first()
        for key, value in new_data.items():
            # audiodata.key= value
            if hasattr(cls, key):
                if value:
                    setattr(audiodata, key, value)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {'username': self.username,
                'email': self.email,
                'id': self.id,
                'password': self.password,
                'first_name':self.first_name,
                'last_name':self.last_name,
                'is_active':self.is_active
                }
