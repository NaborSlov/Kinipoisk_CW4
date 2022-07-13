from flask_restx.reqparse import RequestParser

parser: RequestParser = RequestParser()
parser.add_argument(name='page', type=int, location='args', required=False)
parser.add_argument(name='status', type=str, location='args', required=False)

parser_user: RequestParser = RequestParser()
parser_user.add_argument('email', type=str)
parser_user.add_argument('password', type=str)

