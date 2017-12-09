from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import Youtube_dl


html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf8')
soup = BeautifulSoup(html_content, 'html.parser')

dive = soup.find('div', 'main')
ul = div.find('ul')
li_list = ul.find_all('li')

top_song = []
youtube_list = []
for li in li_list:
    a4 = li.h4.a
    a3 = li.h3.a
    songs = {
        'name': a3.string,
        'singer': a4.string
    }
    top_song.append(songs)
    youtube_list.append('{0} - {1}'.format(a3.string, a4.string))
print(top_song)

pyexcel.save_as(records=top_song, dest_file_name='itune.xlsx')


options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}

dl = YoutubeDL(options)
dl.download(youtube_list)
