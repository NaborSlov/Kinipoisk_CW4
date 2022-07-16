from flask import request, abort

from project.tools.security import decode_token, compose_passwords
from project.container import user_service


def authorizations(func):
    def wrapper(*args, **kwargs):
        access_token = request.cookies.get('AccessToken')

        if not access_token:
            abort(401)

        data = decode_token(access_token)

        user = user_service.get_by_email(data['email'])

        if not compose_passwords(data['password'], user.password):
            abort(401)

        return func(*args, **kwargs, user_id=user.id)

    return wrapper
