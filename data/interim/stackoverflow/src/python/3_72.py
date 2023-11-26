from conf import ma
class UserSchema(ma.SQLAlchemyAutoSchema):
      class Meta:
            model = User
            load_instance = True
