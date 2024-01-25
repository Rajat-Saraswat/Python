# sets -> like mnathematical sets , they cannot have duplicate elements, there is on order

set1 = {'history', 'english', 'hindi', 'maths', 'hindi'}
print(set1)

print('maths' in set1)  # they quilclyt give this result

set2 = {'english', 'physics', 'hindi', 'geography'}

print(set1.intersection(set2))  # gives out the common values
# gives the values in set 1 which are not in set 2
print(set1.difference(set2))

print(set1.union(set2))  # joins the values of both the sets

# emply lists

empty_list = []
empty_list = list()

# empty tuples
empty_tuple = ()
empty_tuple = tuple()

# empty set

empty_set = {}
empty_set = set()
