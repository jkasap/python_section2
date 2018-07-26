import sys
import io
from bs4 import BeautifulSoup as bs


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html", encoding="utf-8")
soup = bs(fp, "html.parser")

'''
f = soup.select_one('div#foods > ul#ac-list > li.alcohol.high')
print(f.string)
'''

print('1 : ', soup.select_one("li:nth-of-type(8)").string)
print('2 : ', soup.select_one('#ac-list > li:nth-of-type(4)').string)
print('3 : ', soup.select("#ac-list > li[data-lo='cn']")[0].string)
print('4 : ', soup.select("#ac-list > li.alcohol.high")[0].string)

param = {'data-lo':'cn', 'class':'alcohol'}
print('5 : ', soup.find('li', param).string)
print('6 : ', soup.find(id="ac-list").find('li', param).string)

for ac in soup.find_all('li'):
    if ac['data-lo'] == 'us':
        print(ac.string)
