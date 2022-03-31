from app.base.models import users as Users
from app.base.schema import usersSchema


def resolve_users(obj, info):
    try:
        users = Users.query.filter_by().all()
        users_schema = usersSchema()
        output = users_schema.dump(users, many=True)

        payload = {
            "success": True,
            "users": output
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def resolve_user(obj, info, id):
    try:
        user = Users.query.filter_by(id=id).first()
        users_schema = usersSchema()
        output = users_schema.dump(user, many=False)

        payload = {
            "success": True,
            "user": output
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
