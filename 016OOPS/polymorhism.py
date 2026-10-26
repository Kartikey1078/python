## Polymorphism ka matlab hai “one name, many forms” — ek hi method ya interface 
# ka different objects ke liye different behaviour hona.

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
          print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()


## polymorphism with inheritence 
class Animal:
     def sound(self):
          return "animals make sound"

class Dog:
     def sound(self):
          return "Dogs make sound"

class Cat:
     def sound(self):
          return "Cats make sound"



animals = [Dog(),Cat(),Animal()]

for animal in animals:
     print(animal.sound())



