from DataBank.Models.Stock.stockDb import Stock
from flask import request, make_response, jsonify
from playhouse.shortcuts import dict_to_model, model_to_dict
from src.config.configApi import app
from peewee import DoesNotExist
from datetime import datetime
def StockRoutes():

    ####################################### Rotas comuns ###############################################################
    @app.route('/stock', methods=['GET'])
    def getStock():
        stock = Stock.select().dicts()
        return make_response(
            jsonify(
                message="Lista de produtos do estoque",
                data=list(stock)
            )
        )


    @app.route("/stock", methods=["POST"])
    def createStock():
        try:
            stock_data = request.get_json()
            stock = dict_to_model(Stock, stock_data)
            stock.save()
            return 'Produto cadastrado com sucesso!', 201
        except Exception as e:
            return f"Houve um erro {e}", 500


    ## Rotas com a necessidade do Parâmetro Id  ##
    @app.route("/stock/<id>", methods=["GET", "PUT", "DELETE"])
    def stock(id):
        if request.method == 'GET':
            try:
                stock = Stock.select().where(Stock.id == id).dicts()

                if not stock:
                    return 'Produto não encontrado', 404

                return make_response(
                    jsonify(
                        message="Produto encontrado",
                        data=list(stock)
                    )
                )
            except Stock.DoesNotExist:
                return "Produto não encontrada", 404
        if request.method == 'PUT':
            try:
                stock_data = request.get_json()
                stock = Stock.select().where(Stock.id == id).get()

                stock.FK_enterprise = stock_data.get('FK_enterprise', stock.FK_enterprise)
                stock.product_name = stock_data.get('product_name', stock.product_name)
                stock.qnt_product = stock_data.get('qnt_product', stock.qnt_product)
                stock.updated_at = datetime.now()

                stock.save()

                return "Produto atualizado com sucesso", 200

            except DoesNotExist:
                return 'Produto não encontrado', 404
            except Exception as e:
                return f"Houve um erro {e}", 500

        if request.method == 'DELETE':
            try:
                stock = Stock.delete().where(Stock.id == id).execute()
                if stock == 0:
                    return 'Produto não encontrado', 404
                return f'Produto de id = {id} deletado com sucesso!'
            except Exception as e:
                return f'Houve um erro {e}', 500

    ####################################################################################################################
