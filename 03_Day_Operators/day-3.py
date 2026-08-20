# # Arithmetic Operations in Python
# # Integers

# print('Addition: ', 1 + 2)
# print('Subtraction: ', 2 - 1)
# print('Multiplication: ', 2 * 3)
# # Division in python gives floating number
# print('Division: ', 4 / 2)
# print('Division: ', 6 / 2)
# print('Division: ', 7 / 2)
# # gives without the floating number or without the remaining
# print('Division without the remainder: ', 7 // 2)
# print('Modulus: ', 3 % 2)                           # Gives the remainder
# print('Division without the remainder: ', 7 // 3)
# print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# # Floating numbers
# print('Floating Number,PI', 3.14)
# print('Floating Number, gravity', 9.81)

# # Complex numbers
# print('Complex number: ', 1+1j)
# print('Multiplying complex number: ', (1+1j) * (1-1j))

# # Declaring the variable at the top first

# a = 3  # a is a variable name and 3 is an integer data type
# b = 2  # b is a variable name and 3 is an integer data type

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
# print(total)  # if you don't label your print with some string, you never know from where is  the result is coming
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# # Declaring values and organizing them together
# num_one = 3
# num_two = 4

# # Arithmetic operations
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_two
# remainder = num_two % num_one

# # Printing values with label
# print('total: ', total)
# print('difference: ', diff)
# print('product: ', product)
# print('division: ', div)
# print('remainder: ', remainder)


# # Calculating area of a circle
# radius = 10                                 # radius of a circle
# # two * sign means exponent or power
# area_of_circle = 3.14 * radius ** 2
# print('Area of a circle:', area_of_circle)

# # Calculating area of a rectangle
# length = 10
# width = 20
# area_of_rectangle = length * width
# print('Area of rectangle:', area_of_rectangle)

# # Calculating a weight of an object
# mass = 75
# gravity = 9.81
# weight = mass * gravity
# print(weight, 'N')

# print(3 > 2)     # True, because 3 is greater than 2
# print(3 >= 2)    # True, because 3 is greater than 2
# print(3 < 2)     # False,  because 3 is greater than 2
# print(2 < 3)     # True, because 2 is less than 3
# print(2 <= 3)    # True, because 2 is less than 3
# print(3 == 2)    # False, because 3 is not equal to 2
# print(3 != 2)    # True, because 3 is not equal to 2
# print(len('mango') == len('avocado'))  # False
# print(len('mango') != len('avocado'))  # True
# print(len('mango') < len('avocado'))   # True
# print(len('milk') != len('meat'))      # False
# print(len('milk') == len('meat'))      # True
# print(len('tomato') == len('potato'))  # True
# print(len('python') > len('dragon'))   # False

# # Boolean comparison
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)
# print('True and True: ', True and True)
# print('True or False:', True or False)

# # Another way comparison
# # True - because the data values are the same
# print('1 is 1', 1 is 1)
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
# print('B in Asabeneh', 'B' in 'Asabeneh')  # False -there is no uppercase B
# # True - because coding for all has the word coding
# print('coding' in 'coding for all')
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# print(3 > 2 and 4 > 3)  # True - because both statements are true
# print(3 > 2 and 4 < 3)  # False - because the second statement is false
# print(3 < 2 and 4 < 3)  # False - because both statements are false
# print(3 > 2 or 4 > 3)  # True - because both statements are true
# print(3 > 2 or 4 < 3)  # True - because one of the statement is true
# print(3 < 2 or 4 < 3)  # False - because both statements are false
# print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# print(not True)      # False - Negation, the not operator turns true to false
# print(not False)     # True
# print(not not True)  # True
# print(not not False)  # False
import math

my_age = 42
print(f'My age is: {my_age}')
my_height = 1.75
print(f'My height is {my_height}m')
my_complex_number = 4j
print(f'My complex number is: {my_complex_number}')

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))

perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}')

length = int(input('Enter the length of a rectangle: '))
width = int(input('Enter the width of a rectangle: '))
area = length * width
print(f'The area of the rectangle is {area}')

radius = int(input('Enter the radius of a circle: '))

pi = 3.14
circle_area = pi * radius * radius
circumference = 2 * pi * radius
print(f'The area of the circle is {circle_area} and the circumference is {circumference}')

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#to calculate euclidean distance, the distance between points p and q is the square root of ((p1 - q1)*2 + (p2 +q2)*2)
x1 = 2
x2 = 2
y1 = 6
y2 = 10
slope = y2-y1/x2-x1
euclidian_calc = abs((x1-y1)*2 + (x2-y2)*2)
euclidian_dist = math.sqrt(euclidian_calc)
print(f'The slope of the given points is: {slope}')
print(f'The Euclidian distance between the given points is: {euclidian_dist}')

print('Are Python and dragon of equal length?')
print(len('python') == len('dragon'))
print("Is 'on' in both python and dragon?")
print('on' in 'dragon' and 'on' in 'python')
#  . Use in operator to check if jargon is in the sentence.
print("Is 'jargon' in the sentence 'I hope this course is not full of jargon.'")
print('jargon' in 'I hope this course is not full of jargon')

# Find the length of the text python and convert the value to float and convert it to string
python_length = len('python')
print(f'The number of characters in "Python" is: {python_length}')
float_convert = float(python_length)
print(f'Convert that number to a float: {float_convert}')
string_convert = str(float_convert)
print(f'Convert that float to a string: {string_convert}')
print(type(string_convert))

print('\n is the floor division of 7 by 3 equal to the integer value of 2.7?')
print(7//3 == int(2.7))

# Check if type of '10' is equal to type of 10
print("Is the type of '10' is equal to the type of 10")
print(type(10) == type('10'))

# Check if int('9.8') is equal to 10
print("\n Is int('9.8') equal to 10?")
print(int(9.8) == 10)
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
time_worked = int(input('Enter Hours: '))
rate = int(input('Enter rate per hour: '))
weekly_earnings = time_worked * rate
print(f'Your weekly earning is {weekly_earnings}')

years_lived = int(input('Enter the number of years you have lived: '))
number_of_seconds = 525600 * years_lived
print(f'You have lived for {number_of_seconds} seconds.')