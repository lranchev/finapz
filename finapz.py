from templates import app
# from flask import Flask
# from alpha_vantage.timeseries import TimeSeries
#
# app = Flask(__name__,
#             static_folder = './public',
#             template_folder="./static"
#             )
#
#
# @app.route('/')
# def index():
#     return "<h1>Deployed to Heroku!</h1>"
#
#
# @app.route('/vlado')
# def vlado_tmp():
#     return "<h1>Vlado's space</h1>"
#
#
# # Plamen's route, yeah babe!!!
# @app.route('/paxi')
# def paxi_tmp():
#     return "<h1>Paxi's space</h1>"
#
#
# # Plamen's route, yeah babe!!!
# @app.route('/lacho')
# def lacho():
#     ts = TimeSeries(key='FH0XYNHWNTKNS1PG')
#     data, meta_data = ts.get_daily('AKAM')
#     return "Lacho's space. \n\n Trying to display some data for AKAM stock here:\n\n" + str(data)


if __name__ == '__main__':
 app.run()