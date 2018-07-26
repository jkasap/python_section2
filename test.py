import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


targetUrl = "http://www2.ticketmonster.co.kr/mart/category/19260000"
savePath = 'c:/mypy/test.html'

parse = req.urlopen(targetUrl).read()
with open(savePath, 'wb') as saveFile:
    saveFile.write(parse)

'''
soup = bs(parse, 'html.parser')

h1 = soup.find_all('em')
print(h1)
'''
