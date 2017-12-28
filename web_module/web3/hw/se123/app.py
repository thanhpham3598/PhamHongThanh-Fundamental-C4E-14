from mlab import mlab_connect
from models.river import River

mlab_connect()

african_rivers = River.objects(continent="Africa")
for river in african_rivers:
    print(river)

samerican_rivers_1000 = River.objects(continent='S. America', length__lt=1000)
for river in samerican_rivers_1000:
    print(river)
