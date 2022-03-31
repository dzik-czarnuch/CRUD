from app import ma
from .models import users
from marshmallow import post_load


class usersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = users

    @post_load
    def create(self, data, **kwargs):
        return users(**data)
