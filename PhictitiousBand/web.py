from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Index page"


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


@app.route('/store')
def store():
    return "Store page"


@app.route('/media')
def media():
    return "Media page"


@app.route('/about')
def about():
    return "About page"


if __name__ == "__main__":
    app.run()
