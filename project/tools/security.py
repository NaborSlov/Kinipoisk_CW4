import base64
import calendar
import datetime
import hashlib
import hmac

import jwt
from flask import current_app, abort


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compose_passwords(password_user: str, password_db: str | bytes):
    return hmac.compare_digest(password_user, password_db)


def decode_token(token: str) -> dict:
    data_user = None
    try:
        data_user = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    except Exception as e:
        print('JWT Decode Error', e)
        abort(401)

    return data_user


def generate_token(data_user: dict) -> dict:
    min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    data_user['exp'] = calendar.timegm(min15.timetuple())
    access_token = jwt.encode(data_user, key=current_app.config['SECRET_KEY'], algorithm='HS256')

    day130 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    data_user['exp'] = calendar.timegm(day130.timetuple())
    refresh_token = jwt.encode(data_user, key=current_app.config['SECRET_KEY'], algorithm='HS256')

    return {'access_token': access_token, 'refresh_token': refresh_token}
