#tuples 

#Access Tuple Items
mytuple = ("apple", "banana", "cherry")
print(mytuple[1])

#negative indexing
print(mytuple[-1])

#range 
print(mytuple[2:5])
print(mytuple[:-1])

#check if item exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change Tuple Values
y = list(mytuple)
y[1] = "kiwi"
x = tuple(y)
