from flask import request
import datetime as dt
from marshmallow import (
    Schema,RAISE,fields,pprint,validate,ValidationError,post_load)
from flask_restplus import Api,Resource

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

class User:
    def __init__(self, name,email,age,permission):
        self.name = name
        self.email = email
        self.age = age
        self.permission = permission
        self.created_at = dt.datetime.utcnow()

    def __repr__(self):
        return "User(name={})".format(self.name)

class Userschema(Schema):
    name = fields.Str(required=True,validate=[validate.Length(min=1)])
    email = fields.Email(required=True,validate=[validate.Length(min=1)])
    permission = fields.Str(validate=[validate.OneOf(["read","write","admin"])])
    age = fields.Int(validate=[validate.Range(min=10,max=30)])

    @post_load
    def make_user(self,data,**kwargs):
        return User(**data)

users = [] 


class UserCollection(Resource):
    def get(self):
        return {"subscriberList":users}

    def post(self,*args,**kwargs):
        schema = Userschema()
        data = request.get_json(force=True)
        errors = schema.validate(api.payload)
        if errors:
            return errors, 422       
        user=schema.load(data)
        result = schema.dump(user)
        users.append(result)

        return {"msg": "Subscriber added"},201


api.add_resource(UserCollection,'/subscribers')


if __name__ == "__main__":
    app.run(debug=True)
