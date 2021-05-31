import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from json import dump,loads,dumps


class UserRegister(Resource):
    def post(self, username=None):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )

        parser.add_argument('email',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )
        parser.add_argument('last_name',
                            type=str,
                            required=False,
                            )
        parser.add_argument('first_name',
                            type=str,
                            required=False,
                            )

        parser.add_argument('is_active',
                            type=bool,
                            required=False,
                            )
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        #data = dumps(data)
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201

    def get(self, username=None):
        user = UserModel.find_by_username(username)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def delete(self, username):
        user = UserModel.find_by_username(username)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted'}, 204
        else:
            return {'message': 'User not found'}, 404

    def put(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=False,
                            help="This field cannot be blank."
                            )
        parser.add_argument('password',
                            type=str,
                            required=False,
                            help="This field cannot be blank."
                            )

        parser.add_argument('email',
                            type=str,
                            required=False,
                            help="This field cannot be blank."
                            )
        parser.add_argument('last_name',
                            type=str,
                            required=False,
                            )
        parser.add_argument('first_name',
                            type=str,
                            required=False,
                            )

        parser.add_argument('is_active',
                            type=bool,
                            required=False,
                            )
        data = parser.parse_args()
        print(data)
        user = UserModel.find_by_username(username)
        if user:
            updated_user = UserModel.update_from_db(username,data)
            return {'message': 'User Updated'}, 204
        else:
            return {'message': 'User not found'}, 404



class UserList(Resource):
    def get(self):
        users = UserModel.get_all()
        data =[]
        if users:
            for user in users:
                data.append(user.json())

            return data
        return {'message': 'User not found'}, 404

