from flask_jwt_extended import JWTManager, create_access_token
from DataBank.Models.User.userDb import User
from flask import request
from src.config.configApi import app
from src.config.generateKey import cipher_suite

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'lkjsa46546werefrg'

def LoginRoute():
    @app.route('/login', methods=['POST'])
    def login():
        user = request.get_json()

        try:
            encrypted_email = cipher_suite.encrypt(user['user_email'].encode())
            encrypted_password = cipher_suite.encrypt(user['user_password'].encode())

            decrypted_users = []
            users = User.select().dicts()
            for user_value in users:
                decrypted_user = {}
                for key, value in user_value.items():
                    if key in ['user_email', 'user_password']:
                        decrypted_user[key] = cipher_suite.decrypt(value.encode()).decode()
                    else:
                        decrypted_user[key] = value
                decrypted_users.append(decrypted_user)

            # Comparar o email descriptografado com o email fornecido nas credenciais de login
            if any(u['user_email'] == cipher_suite.decrypt(encrypted_email).decode() for u in decrypted_users) and any(u['user_password'] == cipher_suite.decrypt(encrypted_password).decode() for u in decrypted_users):
                access_token = create_access_token(identity={'email': user['user_email'], 'name': user_value['user_name']})
                return {'access_token': access_token}
            else:
                    return {'error': 'Credenciais inválidas'}, 401
        except User.DoesNotExist:
            return {'error': 'Usuário não encontrado'}, 401
