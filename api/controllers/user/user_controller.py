# app/controllers/task_controller.py
from flask import jsonify
from api.services.user_service import UserService
from api.serializers.user.user_serializer import UserSerializer
from api.schemas.user.user_schema import UserSchema, CreateUserSchema
from api.schemas.user.user_schema import UpdateUserSchema
from api.errors.not_found_error import NotFoundError
from api.errors.request_validation_error import RequestValidatonError
from api.helpers.request_validator import validate_request_body


class UserController:
    def __init__(self):
        self.userService = UserService()

    def get_all_users(self):
        users = self.userService.get_all_users()

        serialized_users = [UserSerializer.serialize(user) for user in users]

        user_schema = UserSchema(many=True)
        validated_users, errors = user_schema.load(serialized_users)

        if errors:
            return jsonify({"errors": errors}), 422

        return jsonify(validated_users), 200

    def get_user_by_id(self, user_id):
        user = self.userService.get_user_by_id(user_id)
        if user:
            user_serializer = UserSerializer()
            return jsonify(user_serializer.serialize(user=user))
        error = NotFoundError(message="User Not Found")
        return jsonify(error.serialize_error()), error.status_code

    def create_user(self, user_data):
        create_user_schema = CreateUserSchema()
        errors = create_user_schema.validate(user_data)

        if errors:
            validation_error = RequestValidatonError(errors)
            return (
                jsonify(validation_error.serialize_error()),
                validation_error.status_code,
            )

        user = self.userService.create_user(user_data)
        user_serializer = UserSerializer()
        return jsonify(user_serializer.serialize(user)), 201

    def update_user(self, user_id, user_data):
        validation_errors = validate_request_body(user_data, UpdateUserSchema)

        if validation_errors:
            return jsonify(validation_errors), 400

        updated_task = self.userService.update_user(user_id, user_data)
        if updated_task:
            user_serializer = UserSerializer()
            return jsonify(user_serializer.serialize(updated_task))
        error = NotFoundError(message="User Not Found")
        return jsonify(error.serialize_error()), error.status_code

    def delete_user(self, user_id):
        success = self.userService.delete_user(user_id=user_id)
        if success:
            return jsonify({"message": "Task deleted successfully"}), 200
        error = NotFoundError(message="User Not Found")
        return jsonify(error.serialize_error()), error.status_code
