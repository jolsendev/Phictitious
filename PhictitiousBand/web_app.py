from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('in_development.html')


@app.route('/login')
def login():
    return "Login page"


@app.route('/setlists')
def setlists():
    return "Setlist page"


@app.route('/forum')
def forum():
    return "Forum page"


@app.route('/tour_dates')
def tour_dates():
    return "Tour date page"


@app.route('/merchandise')
def merchandise():
    return "Store page"


@app.route('/media')
def media():
    return "Media page"


@app.route('/about')
def about():
    return "About page"


if __name__ == "__main__":
    app.run()
