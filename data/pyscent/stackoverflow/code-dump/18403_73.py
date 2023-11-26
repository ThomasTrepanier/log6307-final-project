from marshmallow_sqlalchemy import ModelSchema
class UserSchema(ModelSchema):
      class Meta:
            model = User
            sql_session = db.session
