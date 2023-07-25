
from flask import Blueprint, request

from app import app
from middlewares.authorise import authorize
from api.controllers.user.user_controller import UserController

user_view = Blueprint("task_view", __name__)


user_controller = UserController()


@app.route("/users", methods=["GET"])
@authorize()
def get_users():
    return user_controller.get_all_users()


@app.route("/users/<int:user_id>", methods=["GET"])
@authorize()
def get_user(user_id):
    return user_controller.get_user_by_id(user_id)


@app.route("/users", methods=["POST"])
@authorize()
def add_user():
    return user_controller.create_user(request.get_json())


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return user_controller.update_user(
        user_id=user_id,
        user_data=request.get_json()
    )


@app.route("/users/<int:task_id>", methods=["DELETE"])
def delete_user(user_id):
    return user_controller.delete_user(user_id=user_id)
