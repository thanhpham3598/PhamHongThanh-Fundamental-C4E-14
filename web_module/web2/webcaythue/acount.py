from mlab import mlab_connect
from models.information import Information
from random import choice, randint
from faker import Faker

information_faker = Faker()

mlab_connect()

for _ in range(10):

    information = Information(name=information_faker.name(),
                              yob=randint(1980,1998),
                              phone="0969696969",
                              city=choice(['Hà Nội','HCM','Đà Nẵng']),)
                              
    information.save()
