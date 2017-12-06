from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.get_default_database()

customers = db['customers']

events = customers.count({'ref':'events'})
wom = customers.count({'ref':'wom'})
ads = customers.count({'ref':'ads'})

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

ref = ['Events', 'Word of Mouth', 'Advertisements']
colors = ['red', 'blue', 'yellow']
total = [events, wom, ads]

for i in range(3):
    for j in range(3):
        if i == j:
            print('{0} has {1} references'.format(ref[i], total[i]))


pyplot.pie(total, labels=ref, colors=colors)
pyplot.axis('equal')
pyplot.show()
