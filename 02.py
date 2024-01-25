# methods in python

message = "Hello World"
# methods on strings -> they are specific functions


print(message.lower())  # to change to lower case
print(message.upper())  # to change to up[pr case
print(message)  # does not manipulate the original string


print(message.count('Hello'))  # gives the amount strings appear in string
print(message.count('l'))
print(message.count('p'))

print(message.find('World'))  # gives the starting index of the input string
print(message.find('o'))
print(message.find('p'))  # gives -1 if not found

# this replaces all the found strings with replacement
print(message.replace('World', 'Universe'))
# does not change the original string
print(message.replace('e', 'hi'))

# to change the original string
message = message.replace('Hello', 'Hi')
print(message)


# concatinating strings

firstName = 'Pogo'
lastName = 'Prakash'

name = firstName + ' ' + lastName
print(name)

# to write bigger string we use formatting strings

greeting = '{} , {}. Welcome!'.format(
    firstName, lastName)  # the {} are placeholders
print(greeting)

# we can also use f strings

# we directly write the variables in place holders
greeting = f'{firstName}, {lastName}. Welcome!'
print(greeting)

# we can use methods directly in f strings
newGreeting = f'{firstName.upper()} , {lastName.lower()} , Welcome!'
print(newGreeting)

# this here gives all the methods that can be used on the input variable , here string
print(dir(name))

# print(help(str))  # this gives hoe methods work on string class
# print(help(str.lower())) #this gives info about specific methods
