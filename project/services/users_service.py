from typing import Optional

from project.dao import UserDAO
from project.exceptions import ItemNotFound, BaseServiceError
from project.models import User
from project.tools.security import generate_password_hash, compose_passwords


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status=None) -> list[User]:
        return self.dao.get_all(page=page)

    def add_user(self, data_user: dict):

        if '' not in data_user.values():
            data_user['password'] = generate_password_hash(data_user.get('password'))
            self.dao.add_user(data_user)
        else:
            raise BaseServiceError('Не введен логин или пароль')

    def user_password_hash(self, data_user: dict) -> bool:
        if '' in data_user.values():
            raise BaseServiceError('Не введен логин или пароль')

        user = self.dao.get_by_email(data_user.get('email'))

        return compose_passwords(data_user.get('password'), user.password)





