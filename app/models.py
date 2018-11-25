from app import login, alchDB
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, alchDB.Model):
    id = alchDB.Column(alchDB.Integer, primary_key=True)
    username = alchDB.Column(alchDB.String(64), index=True, unique =True)
    password_hash = alchDB.Column(alchDB.String(128))

    def __repr__(self):
        return '<User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Blade(alchDB.Model):
    name = alchDB.Column(alchDB.String(16), primary_key=True)
    role = alchDB.Column(alchDB.String(16))
    element = alchDB.Column(alchDB.String(16))
    weapon = alchDB.Column(alchDB.String(16))
    description = alchDB.Column(alchDB.String(128))

    def __repr__(self):
        return '{}'.format(self.name)

class Driver(alchDB.Model):
    name = alchDB.Column(alchDB.String(16), primary_key=True)
    description = alchDB.Column(alchDB.String(128))

    def __repr__(self):
        return '{}'.format(self.name)

class UserBladeLink(alchDB.Model):
    userID = alchDB.Column(alchDB.Integer)
    bladeName = alchDB.Column(alchDB.String(16))
    link = alchDB.Column(alchDB.Integer, primary_key=True)

    def __repr__(self):
        return '{}'.format(self.bladeName)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
