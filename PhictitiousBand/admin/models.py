from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin_app = Admin()

class Person(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(30))

admin_app.add_view(ModelView(Person, db.session))