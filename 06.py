# tuples  -> immutable lists

list_1 = ['history', 'english', 'hindi', 'maths']

list_2 = list_1  # the list 2 is same as list 1
print(list_1)
print(list_2)

list_1[0] = 'Art'  # if l;ist_1 changes then list_2 also changes
print(list_2)

tuple_1 = ('history', 'english', 'hindi', 'maths')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'#we cannnot change the tuple elements as it is immutable
print(tuple_1)
print(tuple_2)
