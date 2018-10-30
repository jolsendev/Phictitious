from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

mod = Blueprint('admin', __name__)

db = SQLAlchemy(mod)

class Person(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(30))