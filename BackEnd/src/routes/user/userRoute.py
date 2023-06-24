from DataBank.Models.User.userDb import User
from flask import request, make_response, jsonify
from playhouse.shortcuts import model_to_dict
from email_validator import validate_email
from datetime import datetime
from src.config.configApi import app
from src.config.generateKey import cipher_suite

def UserRoutes():

    ####################################### Rotas comuns ##############################################################
    @app.route('/user', methods=['GET'])
    def getUsers():
        users = User.select().dicts()
        decrypted_users = []
        for user in users:
            decrypted_user = {}
            for key, value in user.items():
                if key in ['user_email', 'user_password']:
                    decrypted_user[key] = cipher_suite.decrypt(value.encode()).decode()
                else:
                    decrypted_user[key] = value
            decrypted_users.append(decrypted_user)
        return make_response(
            jsonify(
                message="Lista de usuários",
                data=decrypted_users
            )
        )

    @app.route("/user", methods=["POST"])
    def createUser():
        user = request.get_json()

        try:
            if not validate_email(user['user_email']):
                return "Email inválido", 400

            encrypted_email = cipher_suite.encrypt(user['user_email'].encode())
            encrypted_password = cipher_suite.encrypt(user['user_password'].encode())

            decrypted_users = []
            users = User.select().dicts()
            for user_value in users:
                decrypted_user = {}
                for key, value in user_value.items():
                    if key in ['user_email']:
                        decrypted_user[key] = cipher_suite.decrypt(value.encode()).decode()
                    else:
                        decrypted_user[key] = value
                decrypted_users.append(decrypted_user)

            if any(u['user_email'] == cipher_suite.decrypt(encrypted_email).decode() for u in decrypted_users):
                return "E-mail já cadastrado", 400


            User.create(
                user_name=user['user_name'],
                user_email=encrypted_email.decode(),
                user_password=encrypted_password.decode()
            )

            return "Usuário cadastrado com sucesso", 201

        except Exception as e:
            return f"Erro ao cadastrar usuário: {e}", 500

    ####################################################################################################################


    ## Rotas com a necessidade do Parâmetro Id  ##
    @app.route("/user/<id>", methods=["GET", "PUT", "DELETE"])
    def user(id):
        if request.method == 'GET':
            try:
                user = User.get(User.id == id)
                decrypted_user = {}
                for key, value in model_to_dict(user).items():
                    if key in ['user_email', 'user_password']:
                        decrypted_user[key] = cipher_suite.decrypt(value.encode()).decode()
                    elif key == 'created_at':
                        decrypted_user[key] = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        decrypted_user[key] = value
                return make_response(
                    jsonify(
                        message="Usuário encontrado",
                        data=decrypted_user
                    )
                )
            except User.DoesNotExist:
                return "Usuário não encontrado", 404

        if request.method == 'PUT':
            user = request.get_json()

            try:
                # Obter o usuário que será atualizado
                user_to_update = User.get_or_none(id=id)

                # Valida o email recebido na requisição
                encrypted_email = cipher_suite.encrypt(user['user_email'].encode())
                if User.get_or_none((User.user_email == encrypted_email.decode()) & (User.id != id)) is not None:
                    return "Email já cadastrado", 400

                if not validate_email(user['user_email']):
                    return "Email inválido", 400

                encrypted_password = cipher_suite.encrypt(user['user_password'].encode())

                decrypted_users = []
                users = User.select().dicts()

                if user_to_update is None:
                    return "Usuário não encontrado", 404

                # Descriptografa os dados sensíveis dos usuários
                for user_value in users:
                    decrypted_user = {}
                    for key, value in user_value.items():
                        if key in ['user_email']:
                            decrypted_user[key] = cipher_suite.decrypt(value.encode()).decode()
                        else:
                            decrypted_user[key] = value
                    decrypted_users.append(decrypted_user)

                # Verifica se o email já está cadastrado para outro usuário

                for u in decrypted_users:
                    if u['user_email'] == cipher_suite.decrypt(encrypted_email).decode() and u['id'] != user_to_update.id:
                        return "Email já cadastrado", 400

                User.update(
                    user_name=user['user_name'],
                    user_email=encrypted_email.decode(),
                    user_password=encrypted_password.decode(),
                    updated_at=datetime.now()).where(User.id == id).execute()

                return "Usuário atualizado com sucesso", 200

            except Exception as e:
                return f"Houve um erro {e}", 500
            except User.DoesNotExist:
                return "Usuário não encontrado", 404

        if request.method == 'DELETE':
            try:
                user = User.get(User.id == id)
                user.delete_instance()
                return f'Usuário de id = {id} deletado com sucesso!'
            except User.DoesNotExist:
                return "Usuário não encontrado", 404
