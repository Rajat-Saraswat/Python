# conditional statements

if True:
    print('condition was true')

if (3 > 2):
    print('hi')

if (3 < 2):  # since condition is false it will not run
    print('hi')

language = 'python'

if language == 'python':
    print('pyhton')


if language == 'rust':
    print('rust')

if language == 'python':
    print('python')
else:
    print('not python')  # will print else for condition is false

number = 3
number -= 1

if number == 1:
    print(1)
elif number == 2:
    print(2)
elif number == 3:
    print(3)
else:
    print('no mathch')


# boolean operations and ,  or , not

user = 'Admin'
logged_in = True

if (user == 'Admin' and logged_in == True):
    print('can access')
else:
    print('access denied')

if not logged_in:
    print('please log in')
else:
    print('Welcome')


a = [1, 2, 4]
b = [1, 2, 4]

print(a == b)
# this will be false as a and b are different variables and they have different address
print(a is b)


print(id(a))  # gives the address of avriable
print(id(b))


c = b  # now c is equal to b
print(b is c)


# these are the things in python that evaluate to false

# Fale
# None
# zero of any numeric type
# ANY EMPTY SEQUENCE E.G. '', (), []
# any empth mapping e.g. {}
# rest everything is evaluated to true

condition = False
condition = None
condition = 0
condition = 0.1  # this will give true
condition = 0.0  # thsi will give false
condition = ()
condition = []
condition = {}
condition = 'gfhjwa'  # this will be true

if condition:
    print('Evaluated to true')
else:
    print('evaluated to false')
