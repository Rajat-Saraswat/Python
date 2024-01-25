# functions -> sets of codes used to perforn specific tasks
# they promote DRY - Dont Repeat Yourself
def hello_func():  # thsi tells to leave the function empty for now so it does not throws any errors
    pass


hello_func()

# this will give none as function does not have any return value
print(hello_func())
print(hello_func)  # this will give the address of function


def hello():  # definition of function
    print("hello world")


hello()  # function call


def hi():
    return 'Hello Function'


hi()  # this will not give any result as nothing is printed inside function definition

print(hi())  # thsi will print the returned output

print(len('test'))  # the len is also the function

# we can chain functions together

print(hi().upper())  # thsi will return the function in upper case


def add(num1, num2):  # these are the parameters we set to the function, the function can return one value only
    return num1 + num2


# the arguments 2 and 5 will go in the function and sum will be returned
print(add(2, 5))


def greeting(message):
    return '{} Function.'.format(message)


# here message equalt to the variable hi locally, outside the function the message variable is not functional
print(greeting('Hi'))


def greeting2(message, name='You'):  # here the second parameter has a default value of you
    return '{} , {}' .format(message, name)


# if you wont pass the second value it will print you by default
print(greeting2('Hi'))
# if you will give the second value then it will return
print(greeting2('hi', 'tello'))


def student_info(*args, **kwargs):  # these are positional arguments
    print(args)  # return a tuple
    print(kwargs)  # return a dict


student_info('Math', 'Art', name='john', age=22)

courses = ['math', 'arts']
info = {'name': 'pogo', 'age': 22}

student_info(courses, info)  # this would give an empty dict.

student_info(*courses, **info)  # the stars would unpack the values

# number of days per month

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):  # return true for leap else false
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):  # return no of days in a month
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017))
print(is_leap(2024))

print(days_in_month(2017, 2))  # gives days in feb
print(days_in_month(2024, 2))  # gives days in feb
