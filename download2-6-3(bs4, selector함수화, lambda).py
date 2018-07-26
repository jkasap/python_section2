import sys
import io
from bs4 import BeautifulSoup as bs


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html", encoding="utf-8")
soup = bs(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)


#람다식 예제
car_lambda = lambda q : print(soup.select_one(q).string)
car_lambda("#gr")



car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars > #gr")
car_func("#cars #gr")
car_func("li[id='gr']")
