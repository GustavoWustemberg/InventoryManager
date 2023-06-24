from peewee import *
from datetime import datetime
from DataBank.Models.BaseModel.base import BaseModel
from DataBank.Models.User.userDb import User
class Enterprise(BaseModel):
    FK_user = ForeignKeyField(User, backref='user_id')
    name_enterprise = TextField()
    create_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(null=True)