# import flask and flask-restful resources.

from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class HomePage(Resource):
    def get(self):
        return {'Greetings': 'Heelo world!'}

    def post(self):
        print(request)
        return False

class BLQ_investment_calculator(Resource):
    def get(self):
        return 'started BQL investment Calculator'

api.add_resource(HomePage, "/")
api.add_resource(BLQ_investment_calculator, '/blq/investment/calculator')

if __name__== '__main__':
    app.run(debug=True, port=5003)

