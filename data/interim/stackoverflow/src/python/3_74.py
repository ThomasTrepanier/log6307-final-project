from flask_marshmallow import Marshmallow
from .models import Author

ma = Marshmallow()

class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author

    id = ma.auto_field()
    name = ma.auto_field()
    books = ma.auto_field()
