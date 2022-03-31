from ariadne import convert_kwargs_to_snake_case
from app import db
from app.base.models import users as Users
from app.base.schema import usersSchema


@convert_kwargs_to_snake_case
def execute_create_user(_, info, input):
    try:
        user_schema = usersSchema()
        user = user_schema.load(input)
        db.session.add(user)
        db.session.commit()
        output = user_schema.dump(user)

        payload = {
            "success": True,
            "user": output
        }

    except Exception as err:
        payload = {
            "success": False,
            "errors": err
        }

    return payload


@convert_kwargs_to_snake_case
def execute_update_user(_, info, input):
    try:
        user_schema = usersSchema()
        user = user_schema.load(input)
        db.session.merge(user)
        db.session.commit()
        output = user_schema.dump(user, many=False)

        payload = {
            "success": True,
            "user": output
        }

    except AttributeError as err:
        payload = {
            "success": False,
            "errors": err,
        }

    return payload


@convert_kwargs_to_snake_case
def execute_delete_user(obj, info, id):
    try:
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()
        payload = {"success": True}

    except AttributeError as err:
        payload = {
            "success": False,
            "errors": err,
        }

    return payload
