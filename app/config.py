import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = 'this-secret-key'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'var/cw.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
