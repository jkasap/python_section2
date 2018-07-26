import sys
import io
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = bs(html, "html.parser")

links = soup.find_all("a")
"""
a = soup.find_all("a", string="daum")
print(a)
b = soup.find_all("a", limit=3)
print(b)
c = soup.find_all(string=["naver", "google"])
print(c)
"""
#print(type(links))

for a in links:
    #print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print("txt >> ", txt, 'href >> ', href)
