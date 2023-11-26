from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Root(Resource):
    def get(self):
        return {"message": "hello"}


api.add_resource(Root, "/")
