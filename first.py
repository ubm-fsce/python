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
