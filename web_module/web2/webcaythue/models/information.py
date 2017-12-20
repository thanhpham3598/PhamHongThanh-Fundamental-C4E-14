from mongoengine import IntField, StringField, Document

class Information(Document):
    name = StringField()
    yob = IntField()
    phone = StringField()
    city = StringField()
