from flask import Flask
from alpha_vantage.timeseries import TimeSeries


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Deployed to Heroku!</h1>"


@app.route('/vlado')
def vlado_tmp():
    return "<h1>Vlado's space</h1>"


# Plamen's route, yeah babe!!!
@app.route('/paxi')
def paxi_tmp():
    return "<h1>Paxi's space</h1>"


# Plamen's route, yeah babe!!!
@app.route('/lacho')
def lacho():
    return "Lacho's space. \n\n Trying to display some data for AKAM stock here:\n\n" + str(data)
