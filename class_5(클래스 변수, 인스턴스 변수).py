import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NameTest:
    total = 0

print(dir())
print("before: ", NameTest.__dict__)
NameTest.total = 1
print("after: ", NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()

print(id(n1), " vs ", id(n2))  # 서로 다른 인스턴스니까 다른 값이 나옴
print(id(n1.total), " vs ", id(n2.total))   #클래스 변수를 공유하기 때문에 같은 값이 나옴


print(n1.__dict__)  # n1의 네임스페이스 확인 -> 비었음
print(n2.__dict__)  # n2의 네임스페이스 확인 -> 비었음
n1.total = 77       # n1에만 total 값 부여
print(n1.__dict__)  # n1의 네임스페이스 확인 -> tatal:77
print(n2.__dict__)  # n2의 네임스페이스 확인 -> 비었음

print(n1.total)     # n1에는 total값 부여해서 77
print(n2.total)     # n2에는 total값이 없으니 클래스의 total값 1
print(id(n1.total), " vs ", id(n2.total))
print(id(n2.total), " vs ", id(NameTest.total)) # n2가 NameTest의 total값 공유하기에 같음
