class User:
    def __init__(self, name, email, age, gender):
        self.name = name
        self._email = email
        self.age = age
        self.gender = gender

    @property
    def email(self):
        print("Email accessed")
        return self._email
    @email.setter
    def email(self,new_email):
        if '@' in new_email:
            self._email = new_email

# Create person1 object
person1 = User("Rahul", "rahul@gmail.com", 25, "Male")

# Create person2 object
person2 = User("Priya", "priya@gmail.com", 23, "Female")


person1.email = "rah@gmail.com"
print(person1.email)



