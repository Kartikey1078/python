# Python - Access List Items

# Positive indexing
thislist = ["apple", "banana", "cherry"]
oldfruits = ["watermelon"]
thistuple = ("kiwi", "orange")

print(thislist[1])


# Negative indexing
print(thislist[-1])


# Range of indexing
print(thislist[1:3])


# Check if item exists
if "banana" in thislist:
    print("yes this fruit is present")


# Python - Change List Items

thislist[0] = "kela"
print(thislist)


# Insert a new value without changing the existing value
thislist.insert(2, "babugosha")
print(thislist)


# Python - Add List Items

# Append method
thislist.append("aam")  # used to append in the last of the list
print(thislist)


# Insert method
thislist.insert(-1, "jamun")  # used to insert at the specific index of the list
print(thislist)


# Extend method
# [extend method does not append list but also
# extend the list with use tuple, dict, set]
thislist.extend(oldfruits)
print(thislist)

thislist.extend(thistuple)
print(thislist)


# Remove method
# a remove method only remove the first occurance of the value
thislist.remove("cherry")
print(thislist)


# Pop method
# remove the specific index
# if you do not specify the item index it will remove last
thislist.pop(1)


# Del method
# del method remove all list item

# Clear method
# clear method clear all the entires of list

#Python - Loop Lists
for x in thislist:
    print(x)

# looping through index
for i in range(len(thislist)):
    print(i)

#list Comprehension
[print(z) for z in thislist] # shortest way 

# newlist = [expression for item in iterable if condition == True] 
newlist = [x for x in thislist if "a" in x]
print(newlist)

# Python - Sort Lists
thislist.sort()
print(thislist)
# to sort descending
thislist.sort(reverse=True)
print(thislist)
#sort method is case senstive all captial words are stor before the all samler case words.