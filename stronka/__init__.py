from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '0862cdef2c287e81095d38a0380ff9ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///strona.db'
db = SQLAlchemy(app)

from stronka import routes