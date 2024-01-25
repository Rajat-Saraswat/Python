# list and tuples -> they are like arrays in other languages

courses = ['english', 'history', 'maths', 'hindi', 'physics']

print(courses)
print(len(courses))
print(courses[1])
print(courses[-1])  # get last item
print(courses[0])
print(courses[2:])  # from second to last
print(courses[2:4])  # range gives from 2nd to 3rd
print(courses[:3])  # assumes staring from begining

# list methods

# adds element to the end of the list, changes the original list
courses.append('Art')
print(courses)

courses.insert(2, 'Chemistry')  # inserts a value at given location
courses.insert(11, 'Chemistry')  # automatically inserts at end
print(courses)

courses2 = ['music', 'dance']

courses.insert(1, courses2)  # we can add list within a list
print(courses)
print(courses[1])  # gives the entire second list
print(courses[1][0])  # gives the first index of sub list

# to just enter the whole elements of the list within the list independently

# jsut adds the elements of courses2 at the end of initial list
courses.extend(courses2)
print(courses)

courses.remove('Art')  # removes the element given
courses.remove(courses[3])  # removes at the given index
print(courses)

courses.pop()  # removes the last element

print(courses)
popped = courses.pop()  # returns the popped value
print(popped)

courses.reverse()  # reverses the list
print(courses)
