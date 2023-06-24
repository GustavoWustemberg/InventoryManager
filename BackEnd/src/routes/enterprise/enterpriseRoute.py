from DataBank.Models.Enterprise.enterpriseDb import Enterprise
from flask import request, make_response, jsonify
from playhouse.shortcuts import dict_to_model
from src.config.configApi import app
from peewee import DoesNotExist
from datetime import datetime
def EnterpriseRoutes():

    ####################################### Rotas comuns ###############################################################
    @app.route('/enterprise', methods=['GET'])
    def getEnterprise():
        enterprise = Enterprise.select().dicts()
        return make_response(
            jsonify(
                message="Lista de Empresas",
                data=list(enterprise)
            )
        )


    @app.route("/enterprise", methods=["POST"])
    def createEnterprise():
        try:
            enterprise_data = request.get_json()
            enterprise = dict_to_model(Enterprise, enterprise_data)
            enterprise.save()
            return 'Empresa cadastrada com sucesso!', 201
        except Exception as e:
            return f"Houve um erro {e}", 500


    ## Rotas com a necessidade do Parâmetro Id  ##
    @app.route("/enterprise/<id>", methods=["GET", "PUT", "DELETE"])
    def enterprise(id):
        if request.method == 'GET':
            try:
                enterprise = Enterprise.select().where(Enterprise.id == id).dicts()

                if not enterprise:
                    return 'Empresa não encontrada', 404
                return make_response(
                    jsonify(
                        message="Empresa encontrada",
                        data=list(enterprise)
                    )
                )
            except Enterprise.DoesNotExist:
                return "Empresa não encontrada", 404
        if request.method == 'PUT':
            try:
                enterprise_data = request.get_json()
                enterprise = Enterprise.select().where(Enterprise.id == id).get()

                enterprise.FK_user = enterprise_data.get('FK_user', enterprise.FK_user)
                enterprise.name_enterprise = enterprise_data.get('name_enterprise', enterprise.name_enterprise)
                enterprise.updated_at = datetime.now()

                enterprise.save()

                return "Empresa atualizada com sucesso", 200

            except DoesNotExist:
                return 'Empresa não encontrada', 404
            except Exception as e:
                return f"Houve um erro {e}", 500

        if request.method == 'DELETE':
            try:
                enterprise = Enterprise.delete().where(Enterprise.id == id).execute()
                if enterprise == 0:
                    return 'Empresa não encontrada', 404
                return f'Empresa de id = {id} deletado com sucesso!'
            except Exception as e:
                return f'Houve um erro {e}', 500

    ####################################################################################################################
