# integer and floats in python

num = 3
name = ' pogo'
print(num)
print(type(num))  # this gives the type of variable
print(type(name))

num1 = 9
num2 = 4

# Arthemetic operators

print(num1 + num2)  # addition
print(num1 - num2)  # subtraction
print(num1 * num2)  # multiplication
print(num1 / num2)  # division
print(num1 // num2)  # floor division
print(num1 % num2)  # modulus
print(num1 ** num2)  # exponent

print(3 * (2 + 1))  # we can use BODMAS rules here

num += 1  # this is num = num +1
num *= 10  # this is num = num * 1

print(abs(-3))  # this gives abslute values
print(abs(num2 - num1))

print(round(3.556778))  # this rounds off to the nearest integer
print(round(3.556778, 2))  # this rounds of to 2 decimal laces

# Comparision operators

num3 = 2
num4 = 3

r = (num3 == num4)  # checks if equal or not
print(type(r))  # gives out the bool value

print(num3 == num4)
print(num3 >= num4)  # greater or equal
print(num3 <= num4)  # less or equal
print(num3 > num4)  # greater
print(num3 < num4)  # less
print(num3 != num4)  # not equal to

a = '100'
b = '80'  # these ae strings not numbers

print(a + b)  # this will not add but concatinate

# to change them we would typecast them

print(int(a) + int(b))
print(bool(a))
print(a)  # does not change the actual string
