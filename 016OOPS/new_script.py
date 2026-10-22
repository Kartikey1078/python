class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def tell_name(self):
        print(f"hello, my name is kartikey {self.name} and my age is {self.age}")

person1 = Person("Kartikey",26)
person1.tell_name()