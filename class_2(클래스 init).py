import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def __init__(self, name, phone):  #__init__은 초기화 될 때 한 번 실행
        self.name = name
        self.phone = phone

    def print_info(self):
        print("-------------------")
        print("name: ", self.name)
        print("phone: ", self.phone)
        print("-------------------")

    def __del__(self):
        print("delete!")


user1 = UserInfo("kim", "010-1111-1111")
user2 = UserInfo("Park", '010-2222-2222')

print(id(user1))
print(id(user2))

#user1.set_info("kim", "010-1111-1111")
#user2.set_info("Park", '010-2222-2222')

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)
