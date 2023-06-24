import unittest
import json
from src.app import app


class TestOrderRoutes(unittest.TestCase):

    # Define a configuração de testes
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # Testa a rota GET /order
    def test_get_orders(self):
        response = self.app.get('/order')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('data', data)

    # Testa a rota POST /order
    def test_create_order(self):
        payload = {
            "item_description": "Item Teste",
            "item_quantity": 2,
            "item_price": 10
        }
        response = self.app.post('/order', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('item_description', data)

    # Testa a rota GET /order/{id}
    def test_get_order_by_id(self):
        response = self.app.get('/order/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('user_id', data)

    # Testa a rota PUT /order/{id}
    def test_update_order(self):
        payload = {
            "item_description": "Item Teste Atualizado",
            "item_quantity": 3,
            "item_price": 15
        }
        response = self.app.put('/order/1', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('item_description', data)

    # Testa a rota DELETE /order/{id}
    def test_delete_order(self):
        response = self.app.delete('/order/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deletado com sucesso', str(response.data))


if __name__ == '__main__':
    unittest.main()

