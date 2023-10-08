from flask import Flask
from DataBank.initializerDb import initDb

app = Flask(__name__)

def ConfigApi():
    initDb()
    app.config['JSON_SORT_KEYS'] = False
