# strings in python

print("hello World")
print("Hello\n World")  # new line

message = 'Hello World'  # this is a variable name

print(message)
print(message + ' P o g o')

print("Pogo's world")  # if string has single quote, use double quote

print('Pogo\'s World')
# \ is the escape character , the next quote after it does not count

val = input("Enter your value: ")
print(val)  # input in python

print('''Pogo is a good cat
it drinks milk''')  # for multiline printing

print(len("Hello World"))  # the len() function gives the length of the string

print(len(message))

# for accessing the elemnets of the string

print(message[0])  # used to access indices , in python index starts from 0
print(message[4])
print(message[10])  # if some index is out of range it will give error
print(message[-1])  # used to access indices from backwards
print(message[-11])


# we can also get range of indices
print(message[0:7])  # this will give 1st to 6th element, not seventh
print(message[0:])  # it gives all the elements
print(message[5:])  # it gives all the elements
print(message[-9:-3])
print(message[-7:-1])


print("*\n**\n***\n****\n*****\n")
