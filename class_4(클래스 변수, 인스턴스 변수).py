import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 클래스 변수, 인스턴스 변수

class WareHouse:
    stock_num = 0                       #클래스 변수 (인스턴스들에 공유)
    def __init__(self, name):
        self.name = name                #인스턴스 변수 (공유 안됨)
        WareHouse.stock_num += 1

    def __del__(self):
            WareHouse.stock_num -= 1

user1 = WareHouse("kim")
user2 = WareHouse("park")

print(user1.name)
print(user2.name)
print(user1.__dict__)     #인스턴스 변수의 네임스페이스 확인 스 stock_num이 없으나
print(user2.__dict__)     #user1.stock_num을 불러오면 클래스 변수의 stock_num을 가져옴
print(WareHouse.__dict__)

print(user1.stock_num)    #인스턴스 네임스페이스 확인 후 없으면 클래스 네임스페이스 확인,
print(user2.stock_num)    #클래스 변수는 공유됨
