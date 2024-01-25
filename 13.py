# usign the standard library to import functions

import random  # thsi is a module in standard library
import math  # for mathematical calc
import datetime  # for date and time
import calendar  # for calender
import os  # access to the operating system
# import antigravity this opens a comic on browser

courses = ['math', 'english', 'geo', 'his', 'getman']

random_course = random.choice(courses)  # gives random values from the lists
print(random_course)


rads = math.radians(90)  # to convert deg into rad
print(rads)
print(math.sin(rads))  # finding sin

today = datetime.date.today()
print(today)

print(calendar.isleap(2018))
print(calendar.isleap(2020))
print(os.getcwd())  # gives address of current directory
print(os.__file__)  # gives address of current directory file system
