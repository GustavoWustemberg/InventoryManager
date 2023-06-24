from cryptography.fernet import Fernet, InvalidToken
import base64
import os

KEY_FILE = "key.key"

# verificar se o arquivo key.key existe, caso não exista, criar uma nova chave e salvar em arquivo
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
else:
    # ler chave salva em arquivo
    with open(KEY_FILE, 'rb') as f:
        key = f.read()

# criar objeto Fernet com a chave lida
cipher_suite = Fernet(key)

def decrypt_value(value):
    try:
        return cipher_suite.decrypt(value.encode()).decode()
    except InvalidToken:
        return None
