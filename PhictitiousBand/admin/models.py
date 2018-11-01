from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

db = SQLAlchemy()

class Person(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(30))