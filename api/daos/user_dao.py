from api.models.user import User
from app import db


class UserDAO:
    def create_user(self, user_dto):
        user = User(
            name=user_dto.name,
            biopic=user_dto.biopic,
            country=user_dto.country,
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_all_users(self):
        return User.query.all()

    def get_user_country(self, country):
        users = User.query.all()
        return users.join(User.query.get(country))

    def update_user(self, user, user_dto):
        User.name = user_dto.name
        User.biopic = user_dto.biopic
        User.country = user_dto.country
        db.session.commit()

    def delete_user(self, user):
        db.session.delete(user)
        db.session.commit()
