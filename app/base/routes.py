from flask import redirect, url_for
from app.base import blueprint


@blueprint.route("/")
def default():
    return redirect(url_for("api_blueprint.graphql_playground"))
