## Find Largest in List 

nums = [4, 9, 2, 15, 7]
largest = nums[0]

for n in nums:
  if n > largest:
    largest = n

print(largest)


## Greater then any number get the count 
nums = [4, 9, 2, 15, 7]
count = 0
for n in nums:
  if n > 0:
    count +=1

print(count)


## Second Largest 
nums = [10, 5, 20, 8, 15]
largest = float("-inf")
second_Largest = float("-inf")
for n in nums:
  if n > largest:
    second_Largest = largest
    largest = n
    
  elif n < largest and n > second_Largest:
      second_Largest = n


if second_Largest == float("-inf"):
  print("second Largest does not exists")
else:
   print(second_Largest)
      
      
  ## reverse a string

nums = [10, 5, 20, 8, 15]
rev = []

for i in range(len(nums)-1,-1,-1):
    rev.append(nums[i])

print(rev)


## check palidrome 
str = "madam"
store = ""

for char in range(len(str)-1,-1,-1):
    store += str[char]

if store == str:
  print("its is a safe heaven")
else:
  print("I need a cover")
  print(store)


str = "madamm"
char = list(str)

left = 0
right = len(char) - 1

while left < right:
  if(char[right] != char[left]):
    print("Not a Palidrome!!")
    break

  left +=1
  right -=1
else:
     print("Palidrome!!")
  
  
## check a string contain vowels
s = "educationeeee"
count = 0
for char in s:
  if  char in "aeiou":
    count +=1

print(count)


## count number  high case lower case 
s = "Hello WoRld123"
lchar = 0
hchar = 0
nnumber = 0
for char in s:
  if char.isalpha():
    if char.islower():
      lchar += 1
    else:
      hchar += 1
  if char.isdigit():
    nnumber += 1

print(lchar,"lower count")
print(hchar,"upper count")
print(nnumber,"nuber count")



## count frequency in string 

s = "banana"
freq = {}

for char in s:
  if char in freq:
    freq[char] +=1
  else:
    freq[char] = 1
       
print(freq)


## check 2 string are anagram 

# Online Python compiler (interpreter)
# Write and run Python online using this editor.

s1 = "raam"
s2 = "maar"
s3 = "aarm"
s4 = s1 + s2

freq = {}

for char in s4:
  if char in freq:
    freq[char] -= 1
  else:
     freq[char] = 1

if any(value != 0 for value in freq.values()):
    print("Not Anagram")
else:
    print("Anagram")





    
      
    





