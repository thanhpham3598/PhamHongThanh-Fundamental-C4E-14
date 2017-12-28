from mongoengine import *

class Account(Document):
    name = StringField()
    yob = IntField()
    phone = StringField()
    city = StringField()
    pos = IntField()
    credit = IntField()
    occupied = BooleanField()

class Game(Document):
    name = StringField()
    number_players = IntField()
    link_image = StringField()
    link = StringField()
