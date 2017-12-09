from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

html_content = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf8')
file = open('vnm.html', 'w')
file.write(html_content)
file.close

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table','tableContent')
tr_list = table.find_all('tr')

td_data = []
for tr in tr_list:
    td_list = tr.find_all(['td', width:15%;padding:4px;color:014377;', 'width:32%;color:014377;', 'width:15%;padding:4px;color:014377;font-weight:bold;', 'width:32%;color:014377;font-weight:bold;'])
    tr_data = []
    for td in td_list:
        tr_data.append(td.text.strip())
    td_data.append(tr_data)
