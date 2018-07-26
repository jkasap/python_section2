import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def func1():
        print("func1 called")

    def func2(self):
        #print(id(self))
        print("func2 called")


f = SelfTest()   #인스턴스 화
#print(dir(f))

#print(id(f))
f.func1()  #오류 -> 인스턴스에 대한 self 값이 없기 때문에
f.func2()  #정상 -> 인스턴스화해서 self를 매개변수로 받아서
print(SelfTest.func1()) #정상 -> 인스턴스화 하지 않고 클래스 이름으로 접근하여 호출

"""
파이썬 클래스에서 메쏘드를 호출하는 방법은 2개
클래스에 이름으로 직접 접근,
인스턴스화해서"""
