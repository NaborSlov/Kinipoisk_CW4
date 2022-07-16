import string
from typing import Optional

from project.dao import UserDAO
from project.exceptions import ItemNotFound, BaseServiceError
from project.models import User
from project.tools.security import generate_password_hash, compose_passwords, generate_token, decode_token


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status=None) -> list[User]:
        return self.dao.get_all(page=page)

    def get_by_email(self, email: string) -> User:
        return self.dao.get_by_email(email)

    def profile_update(self, user_id: int, data_profile: dict):
        if not any(data_profile.values()):
            raise BaseServiceError('Нет данных')

        user = self.get_item(user_id)
        if not user:
            raise ItemNotFound("Нет такого пользователя")

        if name := data_profile.get('name'):
            user.name = name
        if surname := data_profile.get('surname'):
            user.surname = surname
        if favourite_genre := data_profile.get('favourite_genre'):
            user.favorite_genre = favourite_genre

        self.dao.update(user)

    def password_update(self, user_id: int, data: dict):
        if not all(data.values()):
            raise BaseServiceError('Нет данных')

        user = self.get_item(user_id)
        if not user:
            raise ItemNotFound("Нет такого пользователя")

        hash_password = generate_password_hash(data.get('old_password'))

        if compose_passwords(hash_password, user.password):
            user.password = generate_password_hash(data.get('new_password'))

        self.dao.update(user)

    def add_user(self, data_user: dict):

        if '' not in data_user.values():
            data_user['password'] = generate_password_hash(data_user.get('password'))
            self.dao.add_user(data_user)
        else:
            raise BaseServiceError('Не введен логин или пароль')

    def user_password_verification(self, data_user: dict) -> dict:
        if '' in data_user.values():
            raise BaseServiceError('Не введен логин или пароль')

        user = self.get_by_email(data_user.get('email'))
        data = {'email': user.email,
                'password': user.password}

        if compose_passwords(generate_password_hash(data_user['password']), user.password):
            return generate_token(data)
        else:
            raise BaseServiceError()

    def generate_new_token(self, token: str):
        if not token:
            raise BaseServiceError()

        data = decode_token(token)
        user = self.get_by_email(data['email'])

        if not user:
            raise ItemNotFound("Нет такого пользователя")

        if compose_passwords(data['password'], user.password):
            return generate_token(data)
        else:
            raise BaseServiceError()
