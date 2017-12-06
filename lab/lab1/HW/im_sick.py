from gmail import GMail, Message

reasons = [
    '''<p>Em bị ốm</p>''',
    '''<p>Em bị sốt</p>''',
    '''<p>Em bị ti&ecirc;u chảy</p>''',
    '''<p>Em bị mất tr&iacute; nhớ</p>'''
]
templates = ['''<p>L&iacute; do: {0} .<br />Em hứa sẽ ch&eacute;p b&agrave;i, học b&agrave;i v&agrave; l&agrave;m b&agrave;i tập đầy đủ.</p>
<p>K&iacute;nh mong c&aacute;c thầy c&ocirc; cho em nghỉ buổi học n&agrave;y!</p>''',
'''<p>Em t&ecirc;n l&agrave; Thanh. Em xin nghỉ buổi học h&ocirc;m nay do {0}.</p> ''',
'''<p>Hello c&aacute;c anh c&aacute;c chị h&ocirc;m nay {0} n&ecirc;n em xin nghỉ</p> ''']

from random import choice

reason = choice(reasons)
template = choice(templates)

html_content = template.replace('{0}',reason )

from datetime import datetime

while True:
    time = datetime.now()
    hour = time.hour
    minute = time.minute
    if hour == 21 and minute == 40:
        gmail = GMail('thanhabc35@gmail.com','admin1234')
        msg = Message('XIN CHAO', to = '1234abc@gmail.com',html = html_content)
        gmail.send(msg)
        # print(time)
        break
