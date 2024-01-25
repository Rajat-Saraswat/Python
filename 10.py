
# loops

nums = [1, 2, 3, 4, 5, 6, 7, 8]

for num in nums:  # this will loop and return each itteration
    print(num)

for num in nums:
    if num == 3:
        print('Found')
        break  # this will stop the loop if condition is true
    print(num)


for num in nums:
    if num == 3:
        continue  # this will skip the condition, 3 will not be printed
    print(num)


for num in nums:
    for letter in 'abdsf':
        print(num, letter)  # this is a nested loop


for num in nums:
    if (num == 2):
        print('hi')

for i in range(10):  # this will print 0 to 9, range will give the range from 0 to n-1
    print(i)

for i in range(1, 11):  # we can intitialize the range from a given value
    print(i)


x = 0

while x < 10:  # setting the value
    print(x)
    x += 1  # incrementing x


# if nopt increm,ented it will make an infinite loop

    # while x < 2:
    #     print(x)

while x < 20:
    if x == 12:
        break  # will stop at x =11
    print(x)
    x += 1


# while True:
#     print('hi')  # this will also create a infinite loop
