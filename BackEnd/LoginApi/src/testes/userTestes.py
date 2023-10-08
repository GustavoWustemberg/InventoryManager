import unittest
from flask import Flask, json
from src.app import app

class TestUserRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_create_user_with_valid_data(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'cpf': '12345678901',
            'phone_number': '+5511987654321'
        }
        response = self.client.post('/user', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, 'Usuário cadastrado com sucesso'.encode('utf-8'))

    def test_create_user_with_invalid_email(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoeexample.com',
            'cpf': '12345678901',
            'phone_number': '+5511987654321'
        }
        response = self.client.post('/user', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "Email inválido".encode('utf-8'))

    def test_create_user_with_invalid_cpf(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'cpf': '1234567890',
            'phone_number': '+5511987654321'
        }
        response = self.client.post('/user', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, 'CPF inválido'.encode('utf-8'))

    def test_create_user_with_existing_email(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'cpf': '12345678901',
            'phone_number': '+5511987654321'
        }
        response = self.client.post('/user', json=data)
        response = self.client.post('/user', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, 'E-mail já cadastrado'.encode('utf-8'))

if __name__ == '__main__':
    unittest.main()
