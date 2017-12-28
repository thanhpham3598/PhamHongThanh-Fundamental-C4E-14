import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds111565.mlab.com:11565/caythue

host = 'ds111565.mlab.com'
port = 11565
db_name = "caythue"
user_name = "admin"
password = "admin"

def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
