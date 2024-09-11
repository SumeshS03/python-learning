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
