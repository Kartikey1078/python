
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


