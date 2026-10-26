## A static method on python that reffres to the class itself rather then any instance of any class.
## To define a static method we use '@staticmethod' decorator.
## Jab koi function class se logically related ho, 
# lekin usko object ke attributes (self) ya class attributes (cls) ki zarurat na ho.
class User:
    user_count = 0


    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

        User.user_count += 1

        def display_user(self):
            print(f"User name is {self.name} and email is {self.email}")

        def __check_age(self):
            if age > 20:
                return "age is greater then 20"

user1 = User("kartikey","kartikey@1078",20)
user2 = User("kartikey","kartikey@1078",21)

# print(User.user_count)
print(user2.__check_age())


