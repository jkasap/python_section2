import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("-------------------")
        print("name: ", self.name)
        print("phone: ", self.phone)
        print("-------------------")


user1 = UserInfo()
user2 = UserInfo()

print(id(user1))
print(id(user2))

user1.set_info("kim", "010-1111-1111")
user2.set_info("Park", '010-2222-2222')

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)
