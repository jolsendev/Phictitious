from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "Hello, Anne! You are on the World Wide Web! You're a star!"
if __name__ == "__main__":
  app.run()
