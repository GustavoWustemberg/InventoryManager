from peewee import Model, CharField, DateTimeField, AutoField
from playhouse.mysql_ext import SQL
from DataBank.dbConnection import db

class User(Model):
    user_id = AutoField()
    user_name = CharField(max_length=245)
    user_email = CharField(max_length=245, unique=True)
    user_password = CharField(max_length=245)
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(null=True)

    class Meta:
        database = db
