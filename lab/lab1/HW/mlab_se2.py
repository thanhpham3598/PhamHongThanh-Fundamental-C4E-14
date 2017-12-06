from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title' : 'tình ta biển bạc đồng xanh',
    'author': 'Phạm H Thanh',
    'content':
    '''
    Sao em cứ luôn phải đau buồn thế
    Như bông hoa đang úa tàn gần kề.

    Chuyện tình yêu vốn mãi, vốn mãi luôn đâu phải dễ
    Trăm lời ngọt ngào đi với trăm lời nguyện thề
    Ai biết đâu ai đã đem lòng say mê
    '''
}

posts.insert_one(new_post)
