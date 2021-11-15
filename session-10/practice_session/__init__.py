import os.path

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'H8xOCBC.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

api = Api(app, title="Avocado API")
db = SQLAlchemy(app)

from practice_session.routes import api as ns1

api.add_namespace(ns1)

if __name__ == '__main__':
    app.run(debug=True)
