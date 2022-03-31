from ariadne import (
    make_executable_schema,
    snake_case_fallback_resolvers,
    load_schema_from_path,
    graphql_sync,
    ObjectType
)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from app.api import blueprint

from .queries import resolve_users, resolve_user
from .mutations import execute_create_user, execute_delete_user, execute_update_user

query = ObjectType("Query")
query.set_field("showUsers", resolve_users)
query.set_field("showUser", resolve_user)

mutation = ObjectType("Mutation")
mutation.set_field("createUser", execute_create_user)
mutation.set_field("updateUser", execute_update_user)
mutation.set_field("deleteUser", execute_delete_user)

type_defs = load_schema_from_path("app/api/schema.graphql")

schema = make_executable_schema(
    type_defs, snake_case_fallback_resolvers, query, mutation
)


@blueprint.route("/", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@blueprint.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(schema, data, context_value=request)

    status_code = 200 if success else 400
    return jsonify(result), status_code
