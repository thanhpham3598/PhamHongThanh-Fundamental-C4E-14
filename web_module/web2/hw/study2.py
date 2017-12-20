# import sys
#
# sys.path.append('C4E/lab/')
from mlab import mlab_connect
from service import Service

mlab_connect()

item = Service.objects.get(id='5a3629a0e379421793d100ca')

item.delete()
