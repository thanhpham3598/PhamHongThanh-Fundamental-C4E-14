from mlab import mlab_connect
from models.information import *
from random import choice, randint
from faker import Faker

information_faker = Faker()

mlab_connect()

# Acount
for _ in range(10):
    information = Account(name = information_faker.name(),
                              yob = randint(1980,1998),
                              phone = "0969696969",
                              city = choice(['Hà Nội','HCM','Đà Nẵng']),
                              pos = randint(1,5),
                              credit = randint(1,5),
                              occupied = choice([ True, False ]))

    information.save()

# Game

dota2 = Game(
    name = 'DOTA2',
    link = 'http://127.0.0.1:5000/dota2',
    link_image = 'https://pbs.twimg.com/profile_images/808475349671493632/nvi7WJf4.jpg',
    number_players = randint(0,20)
    )

lol = Game(
    name = 'LOL',
    link = 'http://127.0.0.1:5000/lol',
    link_image = 'http://www.therendezvous.rocks/wp-content/uploads/2015/06/LolPic.jpg',
    number_players = randint(0,20)
    )
csgo = Game(
    name = 'CSGO',
    link = 'http://127.0.0.1:5000/csgo',
    link_image = 'https://pbs.twimg.com/profile_images/531603782690279426/M3dE27yJ_400x400.png',
    number_players = randint(0,20)
    )
csgo.save()
lol.save()
dota2.save()
