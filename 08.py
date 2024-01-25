# dictionaries -> they have key value pairs

student = {
    'name': 'John',
    'marks': 87,
    'age': 22,
    'isMale': True,
    'courses': ['math', 'cs'],
    1: 'sdhgb'
}
# keys can be integers also
print(student)

print(student['name'])
print(student['courses'])  # used to get the specific value

# this will give error print(student['phone']) , as the value does not exist
# to get a  default value and not an error

print(student.get('name'))
print(student.get('phone'))  # gives none for the values not present

print(student.get('phone', 'Not Found'))  # gives specific values

# this will add the key and value in the end of dict.
student['phone'] = '4233463412839428'

student['name'] = 'pogo'  # they are mutable, values can change
print(student)


# this updates the value, it takes in a dictionary
student.update({'name': 'ollie', 'phone': '5t87232', 'age': 24})
print(student)

del student[1]  # used to delete the values and keys

print(student)

popped = student.pop('phone')  # removes the specific element
print(student)
print(popped)  # gives out the removed element


print(len(student))  # gives the number of keys

print(student.keys())  # give sthe keys
print(student.values())  # give the values

print(student.items())  # gives pairs of keys and values

for key in student:  # gives out all the keys
    print(key)

for key, item in student.items():  # gives out both key and the value
    print(key, item)
# we can use any name in place of keys and values
