from peewee import *
from datetime import datetime
from DataBank.Models.BaseModel.base import BaseModel
from DataBank.Models.Enterprise.enterpriseDb import Enterprise
class Stock(BaseModel):
    FK_enterprise = ForeignKeyField(Enterprise, backref='user_id')
    product_name = TextField()
    qnt_product = IntegerField()
    create_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(null=True)