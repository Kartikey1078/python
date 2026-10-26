from datetime import datetime
class Person:
    def __init__(self,name,age,blood_group,gender,phone_number):
        self._phone_number = phone_number
        self.name = name
        self.age = age
        self._blood_group =  blood_group  ## this is just a naming convenction in python 
        # to just tell the devloper not to acces this feild outside, 
        # but natrually python do not through any error over it if we access this outside the 
        ## it is a procted attribute it should'nt be access outside the class
        self.__gender = gender ## use double __ if you want to make it permantely procted 
        ## under the hood python change the name of the attribute and this process in called name mangling.

    def tell_name(self):
        print(f"hello, my name is kartikey {self.name} and my age is {self.age}")

    def blood_group(self):
        return self._blood_group
    
    def get_phoneNumber(self):
        print(f"Email accessed at {datetime.now()}")
        return self._phone_number

    def change_phoneNumber(self,new_phone_number):
        if "+91" in new_phone_number:
            self._phone_number = new_phone_number
        else:
            "not update"


             
    


person1 = Person("Kartikey",26,"o-","m","9999999991")
person2 = Person("Nitish",27,"a+","f","9999999991")
print(person1._blood_group) ## remeber this _ when see this dont access outside 
# print(person1.__gender) ## Now it is completed procted . 
##Now if you try to access the object value then python will throught an error.
print(person2.blood_group())


print(person1.get_phoneNumber())
person1.change_phoneNumber("7015804207")
print(person1._phone_number)






## private use __ and procted use _
# private can't be accessible 
# procted can  be accessible
## use private 