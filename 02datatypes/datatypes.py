
#check and setting the data types

let2 = str("enter the number")
let3 = ["apple",2,"aa"]
let4 = float(20.5)
let5 = list(("apple","banana","cherry"))
let6 = tuple(("apple","banana","cherry"))
let7 = range(6)
let8 = dict(name="john",age=36)
let9 = set(("apple","cherry","banana"))
let10 = bool(5)
let11 = bytes(5)

comman = [ 
let2,
let3 ,
let4 ,
let5 ,
let6 ,
let7 ,
let8 ,
let9 ,
let10,
let11,]

for c in comman:
    print(type(c))




print("=" * 90)
print("         DIFFERENCE BETWEEN LIST, TUPLE, SET AND DICTIONARY")
print("=" * 90)

print(f"{'Feature':<25} {'List':<18} {'Tuple':<18} {'Set':<18} {'Dictionary':<18}")
print("-" * 100)

data = [
    ("Syntax", "[ ]", "( )", "{ }", "{key: value}"),
    ("Ordered", "Yes", "Yes", "No fixed order", "Yes"),
    ("Duplicates", "Allowed", "Allowed", "Not allowed", "Keys unique"),
    ("Mutable", "Yes", "No", "Yes", "Yes"),
    ("Access", "By index", "By index", "No index", "By key"),
    ("Example", "[10, 20, 10]", "(10, 20, 10)", "{10, 20}", '{"name": "Rahul"}'),
]

for row in data:
    print(f"{row[0]:<25} {row[1]:<18} {row[2]:<18} {row[3]:<18} {row[4]:<18}")

print("=" * 100)


