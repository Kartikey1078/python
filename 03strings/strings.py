a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


## string slicing
# You can return a range of character using slice index
b = "hello,world"
print(b[0:5])

#slice from start
print(b[:5])

#slice from the end
print(b[2:])

#negative indexing
print(b[-5:-2])

#upper case
print(b.upper())

#lower case
print(b.lower())

#remove whitespace
print(b.strip())

# replace a string
print(b.replace("h","z"))

#Split string
print(b.split(","))

#string concatinations
print(a + " " +b)

# Python - Format - Strings #
age = 36
earing= 40
txt = f"My name is kartikey,I am {age} years old and i earn {earing:.2f} and per month salary is {earing * 8:.2f}" # 2 f means 2 decimal point 
print(txt)

# Python - String - methods #
new_txt = "Hi this is kartikey "

print(new_txt.lower()) # to lower case
print(new_txt.upper()) # to upper case
print(new_txt.strip()) # remove spacing
print(new_txt.lstrip()) # just remove left side spacing
print(new_txt.rstrip()) # right side spacing removal
print(new_txt.replace("is kartikey","me kartik")) #reomve one text with another
print(new_txt.split()) #convert into list
print(" ".join(new_txt)) #convert a list into string 
print(new_txt.find("k")) #finds is use to find the index/position
print(new_txt.count("i")) #find occurance of a particular number
print(new_txt.startswith("H")) #find a the charter starts with or not
print(new_txt.endswith(" ")) #find a the charter end with or not





