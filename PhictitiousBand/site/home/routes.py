from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint

mod = Blueprint('site', __name__, template_folder="templates", static_folder="static",  static_url_path='/site/home/static')


@mod.route('/')
def index():
    return render_template('index.html')
    # return render_template('in_development.html')

@mod.route('/login')
def login():
    return "Login page"


@mod.route('/setlists')
def setlists():
    return "Setlist page"

@mod.route('/tour_dates')
def tour_dates():
    return "Tour date page"

@mod.route('/media')
def media():
    return "Media page"


@mod.route('/about')
def about():
    return "About page"

