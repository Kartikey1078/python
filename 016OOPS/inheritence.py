## Inheritance ka matlab hai ek class ka doosri
# class ke properties aur methods ko inherit (reuse) karna.


class Animal:
    def eat(self):
        print("animal is eating")

    def sleep(self):
        print("animal is sleeping")
    
class Dog(Animal):
    def bark(self):
         print("Dog is barking")

d = Dog()

d.eat() #inherited from animal
d.sleep() #inherited from anaimal
d.bark() #inherited from dog

