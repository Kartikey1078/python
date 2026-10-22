class Dog:
    def __init__(self,first_name,breed,Owner):
        self.name = first_name
        self.breed = breed
        self.owner = Owner
        

    def bark(self):
        print("Dog is barking")
        
class Owner:
    def __init__(self,owner_name,owner_contact,owner_address):
        self.name = owner_name
        self.contact = owner_contact
        self.address = owner_address
        
owner1 = Owner("kartikey","7015804207","307 p huda sec 12 panipat")
dog1 = Dog('Nitish','Goldern Retriever',owner1)
dog1.bark()
print(dog1.name)
print(dog1.owner.name)

owner2 = Owner("Nitish","9991119990","301 p huda sec 12 panipat")
dog2 = Dog('Ayush','Labradour',owner2)
dog2.bark()
print(dog1.name)
print(dog2.owner.name)