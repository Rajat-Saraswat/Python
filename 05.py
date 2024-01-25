# sorting the list
courses = ['english', 'history', 'maths', 'hindi', 'physics']
courses.sort()  # sorts in alph. order
print(courses)

num = [1, 4, 6, 63, 45, 67, 85, 4, 342, 47, 674, 57, 436, 6]
num.sort()  # sorts in ascending order
print(num)

float = [1.23, 4.5, 364.4, 8.5, 0, 0, 7.63245]
float.sort()
print(float)

courses.sort(reverse=True)
print(courses)  # for descending order

num.sort(reverse=True)
print(num)

print(sorted(courses))  # it does not change the initial list
print(sorted(float))

print(min(num))  # gives max of list
print(max(num))  # gives min of list
print(sum(num))  # gives sum of hte list
print(num)
print(sum(float))

print(max(courses))
print(min(courses))


print(courses.index('maths'))  # gives the index of elements
# print(courses.index('fojaf')) , we will get an erroe if checking for stupid value

print('hindi' in courses)  # gives boolean values
print('hiff' in courses)  # False

for item in courses:  # looping through courses to get all the items
    print(item)

for index, course in enumerate(courses):  # this gives index with item
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)  # this starts the index from 1 instead of 0

# to create list into string

course_str = ', '.join(courses)
print(course_str)  # this will give out the strings with comma seprated values


course_str2 = ' - '.join(courses)
print(course_str2)  # this will give out hyphen seprated values

# this will split out the strings on the given parameter and store as a list
new_list = course_str.split('. ')
print(new_list)
