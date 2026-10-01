def my_function():
    return("hello")


my_function()

print(my_function())


def new_function(name = "kartikey"):
    print("hello "+ name)

new_function(name = "ayush")
new_function()
new_function(name = "niraman")


#sending key words  with key value pair 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# sending data without key words, so thay should be positoned 
#The order matters with positional arguments:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


#Mixing Positional and Keyword Arguments
#However, positional arguments must come before keyword arguments:
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


#Passing Different Data Types
def listdata(data):
   for x in data:
      print(x)

data = [1,3,4,5,5]
listdata(data)