from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Deployed to Heroku!</h1>"


@app.route('/vlado')
def index():
    return "<h1>Vlado's space</h1>"
