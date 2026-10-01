x = lambda a :a+ 10
print(x(5))

x = lambda a , b , c : a * b * c
print(x(2,2,2)) 

#lambda inside a function 
def new_function(n):
    return lambda a : a * n

my_doubler = new_function(2)
print(my_doubler(11))