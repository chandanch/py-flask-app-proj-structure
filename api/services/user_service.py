# app/services/user_service.py
from api.daos.user_dao import UserDAO
from api.dtos.user.user_dto import UserDTO


class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, user_data):
        user_dto = UserDTO(**user_data)
        return self.user_dao.create_user(user_dto)

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def update_user(self, user_id, user_data):
        user = self.user_dao.get_user_by_id(user_id)
        if user:
            user_dto = UserDTO(**user_data)
            self.user_dao.update_user(user, user_dto)
            return user
        return None

    def delete_user(self, user_id):
        user = self.user_dao.delete_user(user_id)
        if user:
            self.user_dao.delete_user(user)
            return True
        return False
