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
# j is local vairable here so we expect a NameError: name 'j' is not defined
# if any exception  the flow stops and program exits.
#print(j)
# as k is global this is accessible
print(k)
