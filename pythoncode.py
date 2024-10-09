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

#two table using for loop
i=2
for j in range (1,11):
   print(f"{i} * {j} = {i*j}")

#between two number using for loop
a=int(input("enter first number:"))
b=int(input("enter second number:"))
for i in range(a+1,b):
   print(i)

#even number between 1 to 10
for i in range(1,11):
   if(i%2==0):
      print(i)
      
#odd number between 1 to 10
count = 0
for i in range(1,11):
   if(i%2 != 0):
      print(i)
      count =count + 1
print("the number of odd number count:",count)
   
#count number div by 3 and 5 and both range 1-100
three_count = 0
five_count = 0
count=0
for i in range(1,101):
   if(i%3==0 and i%5==0):
      print(i)
      count = count + 1
   elif(i%3 == 0):
      print(i)
      three_count =three_count + 1
   elif(i%5 == 0):
      print(i)
      five_count =five_count + 1
  
print("the number div by three:",three_count)
print("the number div by five:",five_count)
print("the number div by both:",count)

#sum of first 5 natural numbers
sum = 0
for i in range(1,6):
   sum = sum + i
print(sum)
   
#10 input from user and add and average
a=[]
c=0
for i in range(10):
   b=int(input("enter the number:"))
   a.append(b)
   c = c+b
print(a)  
print("sum of ten numbers:",c)
print("average",int(c/10))

#print natural number and their sum
a=int(input("enter the number:"))
b=0
for i in range(a):
   print(i+1)
   b = b + i+1
print("sum of natural number:",b)

#cube upto enter number
a=int(input("enter the number:"))
for i in range(a):
   print(f"cube of number {i+1} : {(i+1)**3}")

#pattern printing
for i in range(5):
   print()
   for j in range(1,i+1):
      print(j,end ="")
   
      
#while loop to print 1-5
i=1
while(i<=5):
   print(i)
   i = i+1
   
#while loop to print 10.20.30...200
i=10
while(i<=200):
   print(i,end =",")
   i = i+10
      
#while loop reverse order of 10 
i=10
while(i>= 1):  
    print(i,end =",")
    i=i-1

#while loop factorial of number 
i=int(input("enter the number:"))
fact = 1
while(i>0):
   fact = fact*i
   i = i-1
print(fact)
      
#fuctions add,sub,mul,div
def add(a,b):
   print(a+b)
def sub(a,b):
   if(b>a):
      print(b-a)
   else:
      print(a-b)
def mul(a,b):
   print(a*b)
def div(a,b):
   print(int(a/b))
a=10
b=20
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)

#input from user and passit to fuction find even or odd
def findevenorodd(a):
   if(a%2==0):
      print("enter number is even")
   else:
      print("enter number is odd")
a=int(input("enter the number:"))
findevenorodd(a)

#input from user find pass or fail
def findevenorodd(a):
   if(a>=35 and a<=100):
      print("you are pass")
   elif(a<35):
      print("you are fail")
   elif(a>100):
      print("invalid mark")
a=int(input("enter the mark:"))
findevenorodd(a)

#input from user print the range
def printrange(a,b):
   for i in range(a,b):
      print(i)
a=int(input("enter the a:"))
b=int(input("enter the b:"))
printrange(a,b)

#input from user check username password
def validate(s_username,s_password,name,code):
   if(s_username==name and s_password==code):
      return True
   else:
      return False
   
s_username="sumesh"
s_password=123
name=str(input("enter the username:"))
code=int(input("enter the password:"))
print(validate(s_username,s_password,name,code))

#input from user a+b*c
def add():
   return (a+b)*c
   
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the c value:"))
d=add()
added=add()
print(added)
print(d)

#class and objects
class laptop:
   price=""
   processor=""
   ram=""
hp = laptop()
dell = laptop()
lenovo = laptop()
hp.price = 40000
hp.processor= "core i3"
hp.ram = "8GB"
dell.price = 50000
dell.processor = "core i5"
dell.ram = "12GB"
lenovo.price = 60000
lenovo.processor = "core i7"
lenovo.ram = "16GB"
print("hp laptop price:",hp.price)
print("hp processor:",hp.processor)
print("hp ram:",hp.ram)
print("lenovo laptop price:",lenovo.price)
print("lenovo processor:",lenovo.processor)
print("lenovo ram:",lenovo.ram)
print("dell laptop price:",dell.price)
print("dell processor:",dell.processor)
print("dell ram:",dell.ram)

#class and objects using constructor
class student:
   def __init__(self):
      name=""
      reg_num=""
   def display(self):
      print("student name:",self.name)
      print("student reg no:",self.reg_num)
      
school= student()
school.name = "sumesh"
school.reg_num = 1546
school.display()

#class and objects using constructor
class teacher:
   def __init__(self):
      name=""
      register=""
   def display(self):
      print("name of the teacher:",self.name)
      print("register no of the teacher:",self.register)

t1=teacher()
t2=teacher()
t1.name="jeni"
t1.register=231
t2.name="janu"
t2.register=432
t1.display()
t2.display()

#class and objects using constructor
class calculator:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def add(self):
      print("added number:",self.a+self.b)
   def sub(self):
      if(self.b>self.a):
         print("subracted number:",self.b-self.a)
      else:
         print("subracted number:",self.a-self.b)
   def mul(self):
      print("multiplied value:",self.a*self.b)
   def div(self):
      if(self.a==0 or self.b==0):
         print("invalid")
      else:
         print("divided value is:",self.a/self.b)
c=calculator(2,3)
c.add()
c.sub()
c.mul()
c.div()

#polymorphism function overwrite
class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Birds sing")

c=animal()
c1=dog()
c2=bird()
c.sound()
c1.sound()
c2.sound()


#polimorphism rectangle problem
class shape:
   def area(self):
      return 
class rectangle(shape):
   def area(self):
      l=10
      b=20
      print(l*b)
a1=rectangle()
a1.area()
   
#polimorphism and superkeyword
class person:
    def __init__(self):
        self.name = ""

class student(person):
    def __init__(self):
        super().__init__() 
        self.grade = ""
    def display(self):
        print(self.name)
        print(self.grade)
c = student()
c.name = "sumesh"
c.grade = "a+"
c.display()

#polimorphism overwrite
class vehicle:
   def start(self):
      print("vehicle started")
class car(vehicle):
   def start(self):
      print("car started")
c=car()
c.start()

#polimorphism overwrite
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

e = Manager(name="Sumesh", salary="12000", department="Production")
e.display()

#leetcode problems
#two sum
class Solution:
    def twoSum(self, nums: [int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return(seen[complement],i)

            seen[num] = i
solution = Solution()
nums = [2,5,7,4,6,1,8]
target = 9
print(solution.twoSum(nums,target))
#Palindrome

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x!=0 and x%10==0:
            return False
        reversed = 0
        while x > reversed :
            reversed = reversed * 10 + x%10
            x = x // 10

        return x == reversed or x == reversed // 10

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
        