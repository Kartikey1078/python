# Python - Access Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:

# to access the key of dict
x = thisdict.keys()
# to access values
x = thisdict.values()

thisdict["year"] = "2026" # change in original srting will reflect in original dict.

x = thisdict.items()# print in key value pair as a tuple in a list 
print(x)

# check if key exists in dictt
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#update the dictt
thisdict.update({"year":2025})
print(thisdict)

#remove item 
thisdict.pop("year")
