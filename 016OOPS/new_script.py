class Person:
    def __init__(self,name,age,blood_group,gender):
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

person1 = Person("Kartikey",26,"o-","m")
person2 = Person("Nitish",27,"a+","f")
print(person1._blood_group) ## remeber this _ when see this dont access outside 
print(person1.__gender) ## Now it is completed procted . 
##Now if you try to access the object value then python will throught an error.

