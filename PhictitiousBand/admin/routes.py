from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint
from flask_admin import Admin

mod = Blueprint('admin', __name__)