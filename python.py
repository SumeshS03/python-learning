greeting_message = "welcome sumesh"
todays_date = 10
print greeting_message 
print todays_date


product = 3*7
print product
remainder =1398%11
print remainder


january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall
print annual_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall
print annual_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall
print annual_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06
annual_rainfall += september_rainfall + october_rainfall +november_rainfall + december_rainfall
print annual_rainfall

#this variable describe the city name:
city_name = "St. Potatosburg"

# this variable describe the city population: 
city_pop = 340000

cucumbers =5
price_per_cucumber=3.25
total_cost=5*3.25
print total_cost


cucumbers=100
num_people=6
whole_cucumbers_per_person=cucumbers/num_people
print whole_cucumbers_per_person
float_cucumbers_per_person=float(cucumbers)/num_people
print float_cucumbers_per_person

haiku="""The old pond,
A frog jumps in:
Plop!"""
print haiku

float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
x=product
big_string = " The product was " + str(x)
print big_string

skill_completed = "Python Syntax"
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed*points_per_exercise
print " I got "+str(point_total)+" points! "

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

the_machine_goes = "Ping!"
print the_machine_goes

my_string = "my name is sumesh"
print len(my_string)
print my_string.upper()

from datetime import datetime
print datetime.now()
now = datetime.now()
print now

from datetime import datetime
print datetime.now()
now = datetime.now()
print now.year
print now.month
print now.day


from datetime import datetime
now = datetime.now()
print '%d/%d/%d' % (now.month, now.day, now.year)


from datetime import datetime
now = datetime.now()

print '%02d-%02d-%04d' % (now.month, now.day, now.year)

print now.hour
print now.minute
print now.second

print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

from datetime import datetime
now = datetime.now()
print now.hour
print now.minute
print now.second
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
    print grade_converter(92)
    print grade_converter(70)
    print grade_converter(61)

original = raw_input("Enter a word:")
if len(original) > 0:
  print original
else:
  print "empty"
  
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty"


pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
    
    
pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word + first + pyg
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
print new_word


pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
    print 'empty'
    
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
square(10)

def power(base, exponent): 
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(2, 4) 


def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

import math
print math.sqrt(25)


def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
  
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena"
zoo_animals[3] = "lion"

suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("sumesh")
suitcase.append("logesh")
suitcase.append("harish")
list_length = len(suitcase)
print "There are %d items in the suitcase." % (list_length)
print suitcase

start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()
print square_list

menu = {} 
menu['Chicken Alfredo'] = 14.50 pair
print menu['Chicken Alfredo']
menu['Spam'] = 2.50
menu['food'] = 4.90
menu['rice'] = 4.90
print "There are " + str(len(menu)) + " items on the menu."
print menu

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Plains Exhibit'

print zoo_animals

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], 
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort() 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50


names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
    print(name)
    
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for word in webster:
  print webster[word]
  
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
  if number % 2 == 0:
    print number
    
    
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count
print fizz_count(["fizz","cat","fizz"])


for letter in "Codecademy":
  print letter
print
print

word = "Programming is fun!"

for letter in word:
 
  if letter == "i":
    print letter
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
  print food
  print "price: %s" % prices[food]
  print "stock: %s" % stock[food]
total = 0
for food in prices:
  print prices[food] * stock[food]
  total = total + prices[food] * stock[food]
print total

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [lloyd, alice, tyler]

avg = get_class_average(students)
print(avg)
print(get_letter_grade(avg))

n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
print double_list(n)

n = ["Michael", "Lieberman"]


def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print join_strings(n)

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)

count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

while count < 10:
  print "Hello, I am a while and count is", count
  count += 1
  
from random import randint


random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."

phrase = "A bird in the hand..."
for char in phrase:
  if char == "A" or char == 'a':
    print 'X',
  else:
    print char,
print

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num
for num in numbers:
  print num ** 2
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' 
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'