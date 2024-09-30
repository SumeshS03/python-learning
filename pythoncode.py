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
   
   
#casting
x = int("10")
y = int("20")
z = x+y
print(z)


#input from user
x=int(input())
y=int(input())
z=x+y
print(z)

#first program
x=str(input())
y=int(input())
print("My name is:",x)
print("My age is:",y)

#second program
x=str(input())
y=int(input())
z=str(input())
print("My name is:",x)
print("My age is:",y)
print("My address:",z)

#third program
x=int(input())
y=int(input())
z=int(input())
a=x*y*z
b=x+y+z
c=a/b
print(a)
print(b)
print(c)

#fourth program
name=str(input())
score=int(input())
department=str(input())
a=score/10
print("My name is",name)
print("My score is",a,"/10")
print("My department is",depart)

#if else concept
three=input("enter the number three:")
if three==3:
   print("yes the number is three")
else:
   print("the number is not three")

#first program

mark=int(input("enter ypur mark:"))
if (mark > 35):
   print("pass")
else:
   print("fail")

#number is divisible by 5 and 3
number=int(input("enter your number:"))
if (number%3==0 and number%5==0):
   print("the number is divisible by 3 and 5")
else:
   print("the number is not divisible by 3 and 5")
   
   
#number is odd or even
number=int(input("enter your number:"))
if (number%2==0):
   print("the number is even")
else:
   print("the number is odd")


#student score
score=int(input("enter your score out of 100:"))
if (score<35):
   print("poor student")
elif (score>35 and score<70):
   print("average student")
elif (score>70 and score<=100):
   print("good student")
else:
   print("invalid score")

#mini calculator
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
a=str(input("enter whether to add/sub/mul/div :"))
if(a == "add"):
   print("added number is:", num1+num2)
elif(a == "sub"):
   if(num2>num1):
      print("subtracted number is:", num2-num1)
   else:        
      print("subtracted number is:", num1-num2)
elif (a == "mul"):
   print("multiplied number is:", num1*num2)
elif (a == "div"):
   print("divided value is:", num1/num2)
else:
   print("invalide input")
   
#elgible or not
score=int(input("enter your score percentage:"))
if(score>70):
   a=input("enter your name:")
   b=input("enter your department:")
   c=input("enter your location:")
   print("you are eligibile")
else:
   print("you are not eligibile")

#loan eligibile or not

a=int(input("enter your salary:"))
b=int(input("enter your age:"))
if(a>=20000 or b<=25):
   loan=int(input("enter your loan amount:"))
   if(loan<=50000):
      print("you are eligible for loan")
   else:
      print("maximum loan amount is 50000")
else:
   print("you are not elgibile")

#five subject mark

a = int(input("Enter your mark for subject 1: "))
b = int(input("Enter your mark for subject 2: "))
c = int(input("Enter your mark for subject 3: "))
d = int(input("Enter your mark for subject 4: "))
e = int(input("Enter your mark for subject 5: "))
f = a+b+c+d+e
avg = f/5
if(avg<35):
   print("Additional class is Required")
else:
   print("you are good to go")

