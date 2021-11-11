import os.path
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
api = Api(app, title="Book API")
db = SQLAlchemy(app)

import flaskProjectTest.routes

if __name__ == '__main__':
    app.run(debug=True)
