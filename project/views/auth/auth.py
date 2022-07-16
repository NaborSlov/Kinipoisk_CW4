from flask import request
from flask_restx import Namespace, Resource
from project.setup.api import pr_user
from project.container import user_service

api = Namespace('')


@api.route('/auth/register/')
class RegisterView(Resource):
    @api.expect(pr_user)
    def post(self):
        user_service.add_user(pr_user.parse_args())


@api.route('/auth/login/')
class AuthsView(Resource):
    @api.expect(pr_user)
    def post(self):
        return user_service.user_password_verification(pr_user.parse_args())

    def put(self):
        refresh_token = request.cookies.get('RefreshToken')
        return user_service.generate_new_token(refresh_token)
