from DataBank.Models.User.userDb import User
from DataBank.dbConnection import db

def initDb():
    db.connect()
    db.create_tables([User], safe=True)
