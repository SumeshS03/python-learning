print("Hello, World!")
#This is a comment
"""
This is a comment
written in
more than just one line
"""

x = 10
y = "string"
print(x)
print(str(y))
x = str(10)
x = float(10)
#datatype
x = 10
y = "string"
print(type(x))
print(type(y))

#assign multiple values to different variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#assign multiple values to same variable
x = y = z = "Orange"
print(x)
print(y)
print(z)
#collection of values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#multiple values output separated by comma
x = maths
y = is my
z = fav subject
print(x, y, z)
#multiple values output separated by + operator
x = maths
y = is my
z = fav subject
print(x + y + z)

#variable outside 
x = "subject"

def myfunc():
   print("maths is a" + x)

myfunc()
#variable inside
x = "subject"

def myfunc():
   x = "good"
   print("maths is a" + x)

myfunc()
   print("maths is a" + x)
#global variable
x = "subject"

def myfunc():
   global x
   x = "good"
   print("maths is a" + x)

myfunc()
   print("maths is a" + x)