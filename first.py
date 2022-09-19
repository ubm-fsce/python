import random
from contextlib import nullcontext

print("======Begin=====")
a = 3
b = "john"
print(a + a)
#  this is Comment
if 10 > 5:
    print("5 is big")
"""
This is MultiLine Commennts 
print ("2 is big")
"""
print("6 is big")
print("a : ", a)
print("Type a : ", type(b))
c = str(a)
print("c : ", c)
print(" Typec : ", type(c))

if "john" == 'john':
    print("Both john and John are same")

A = "john"

if b == A:
    print("A and b are Same")

x = y = z = "apples"
print("x : ", x, "| Y : ", y, " | Z : ", z)

fruits = ["orange", "apple", "bananna"]
d, m, z = fruits
print("fruits =>", fruits)
print(d)
print(m)
print(z)


def func():
    j = "is fantastic"
    global k
    k = "is GOOD"
    print(A, k, j)


func()

print(k)
"""
# j is local vairable here so we expect a NameError: name 'j' is not defined
# if any exception  the flow stops and program exits.
print(j)
# as k is global this is accessible
"""
print(k)

a = """adfadsfafa
adfadsfa
adsfafda
asdfaf
adfaaf"""
print("a==> ", a)

X = "Hell0"
print("1 Hello Type ==>", type(x))
x = 20
print("22 0 Type : ", type(x))
x = 20.5
print("3 20.5 Type : ", type(x))
x = 1j
print("ij Type : ", type(x))
x = ["apple", "banana", "tomoto"]
print("4 : Type : ", type(x))
x = ("apple", "banana", "tomoto")
print("5 : Type : ", type(x))
x = range(6)
print("6 : Type : ", type(x))
x = {"name": "john", "age": 32}
print("7 : Type : ", type(x))
x = {"app", "app", "app"}
print("8 : Type : ", type(x))
x = frozenset(x)
print("9 type : ", type(x))
x = True
print("10 type : ", type(x))
x = b"Hellp"
print("11 type : ", type(x))
x = bytearray(10)
print("12 type : ", type(x))
x = None
print("13 type : ", type(x))
x = str("Hello")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana"))
x = tuple(("apple", "banana"))
x = range(8)
x = dict(name="jo", age=14)

x = 1.0
y = 333.33333333333333333333333333333333333333
z = -2.22222
print("x type: ", type(x), "y type : ", type(y), "z type : ", type(z))

print("x float: ", float(x), "y int : ", int(y), "z complex : ", complex(z))

print(random.randrange(1, 3000))

a = "HellO world!   "
print("a[1] is :=> ", a[1])

for x in a:
    print(x)

print(" length of 'HELLO WORLD' IS ", len(a))

print("hel" in a)
print("Hel" in a)

if "Hel" in a:
    print("Yes Hel is present in ", a)
if "HEL" not in a:
    print("HEL is not present in ", a)

## Slicing of Text
print(a, "a[:2]", a[:2])
print(a, "a[2:]", a[2:])
print(a, "a[1:2]", a[1:2])
print(a, "a[-5:-1]", a[-5:-1])
print(a, "a[1:5:2]", a[1:5:2])

## Modify Strings

print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("l", "U"))
print(a.split(" "))
## Format Strings
age = 36
#txt = "My name is John, I am " + age

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
# Strings
name = "Sam"
for x in name:
    print(x)
#SLICE
last_letters = name[1:]
name = "P" + last_letters
print(name)

name = name + " " + " " + name + " " + name + " " + " "
print(name)

print("Hello[1] : => ", "Hello"[1])

print("SAMMY[2:]  :=>", "SAMMY"[2:])

print('2' + '3')
# SPLIT
name = "Hi This is a String"
print(name.split('i'))

# Print FORMATTINg Sting
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("this is string {}".format('INSERTED'))

print('the {} {} {}'.format('fox', 'brown', 'fox'))

print('The {f} {b} {q}'.format(f='fox', b='box', q='quick'))

# Floating point precision
result = 100 / 7777
print('100/7777 :=>', result)
print('The result was {r:10.3f}'.format(r=result))
print('The result was {r:0.3f}'.format(r=result))

# f String format
name = "jeoseph"
print(f'hello,  his name is {name}')
age = 3
print(f'name : {name}, age : {age}')

# LISTS IN PYTHON
my_list = [1, 2, 3]
my_list_2 = [1, "lk", 12.222, 123]
print(len(my_list))
print(len(my_list_2))
print(my_list[1])
print('my_list + my_list_2', my_list + my_list_2)
new_list = my_list + my_list_2
print('new_list', new_list)
print(new_list[0] == "ALL_CAPS")

txt = "Hello World"
print("txt[2:4]", txt[2:5])
thislist = ['apple', 'banana', 'cherry']
print("Lenght of List ['apple', 'banana', 'cherry'] : ", len(thislist))
# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print("list1 Type : ", type(list1))
# Access Elements in the list
print("thislist[0] :", thislist[0])
print("['apple', 'banana', 'cherry']  last Element : ", thislist[-1])

print("['apple', 'banana', 'cherry'] 2-4 elements :  ", thislist[2:4])
#Change list Items
if 'apple' in thislist:
    print("Apple is in the list")

thislist[1:3] = ['item1', 'item2']
print("This List after updated : ", thislist)

thislist.insert(0, 'item0')
print("This list after insert @ 0 : ", thislist)
thislist.append('item3')

print("This list after append : ", thislist)
