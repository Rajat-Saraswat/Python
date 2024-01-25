# the name of the file shouls be my_module and it should be in the same directory
# if not in same directory, we can add sys.path.append('/Users/rajatsaraswat/Desktop/my_module)

import my_module as mm  # we give an abbrn. to using mymodule
# for specific function, we can say "from my_module import find_index"
# for multiple items we use from my_mode import find_index as fi, test
# to import everything  from my_module import *

import sys
courses = ['math', 'history', 'art', 'english']

# index = my_module.find_index(courses, 'math') #using the find function from my  module
# print(index)


# using the find function from my  module
index = mm.find_index(courses, 'math')  # using the mm abriviation
print(index)

print(sys.path)  # this gives the list of directories added to python path enviornment
