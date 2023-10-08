from peewee import SqliteDatabase
from DataBank.Models.User.userDb import User
from DataBank.Models.Enterprise.enterpriseDb import Enterprise
from DataBank.Models.Stock.stockDb import Stock

def initDb():
    db = SqliteDatabase("stock.db")

    db.connect()
    db.create_tables([User, Enterprise, Stock])
