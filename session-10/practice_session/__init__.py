import os.path
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'H8xOCBC.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=5)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(seconds=10)

jwt = JWTManager(app)
api = Api(app, title="Avocado API")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from practice_session.routes import api as ns1

api.add_namespace(ns1)

if __name__ == '__main__':
    app.run(debug=True)
