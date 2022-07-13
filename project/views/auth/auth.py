from flask_restx import Namespace, Resource
from project.setup.api import parser_user
from project.container import user_service

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.expect(parser_user)
    def post(self):
        user_service.add_user(parser_user.parse_args())


@api.route('/login/')
class AuthsView(Resource):
    @api.expect(parser_user)
    def post(self):
        if user_service.user_password_hash(parser_user.parse_args()):
            return 200
        else:
            return 404, 'Неправильный логин или пароль'


