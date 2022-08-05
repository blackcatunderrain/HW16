from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///databases.db'

db = SQLAlchemy(app)

