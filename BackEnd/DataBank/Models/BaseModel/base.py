from peewee import *

db = SqliteDatabase("stock.db")

class BaseModel(Model):
    class Meta:
        database = db