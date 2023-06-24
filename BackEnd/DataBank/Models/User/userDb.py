from peewee import *
from datetime import datetime
from DataBank.Models.BaseModel.base import BaseModel

class User(BaseModel):
    user_name = TextField()
    user_email = TextField(unique=True)
    user_password = TextField()
    create_at = DateField(default=datetime.now())
    updated_at = DateTimeField(null=True)
