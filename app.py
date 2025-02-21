from flask import Flask, render_template, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Rest(Resource):
    def get(self):
        return {'rest':'OK'}

api.add_resource(Rest, '/')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)