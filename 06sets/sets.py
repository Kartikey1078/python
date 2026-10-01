thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]
for x in thisset:
  print(x)

#check if banana is presnt 
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#check if banana is not presnent
print("banana" not in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
thisset.add("JAMUN")
print(thisset)

#To add items from another set
thisset.update(tropical)
print(thisset)

#update any iterable object
thisset.update(mylist)
print(thisset)

# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana") # if not banana is presnt this it will give error 
print(thisset)

thisset.discard("banana")
print(thisset)