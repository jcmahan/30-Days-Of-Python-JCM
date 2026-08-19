# Introduction
# Day 1 - 30DaysOfPython Challenge

# print("Hello World!")   # print hello world

# print(2 + 3)   # addition(+)
# print(3 - 1)   # subtraction(-)
# print(2 * 3)   # multiplication(*)
# print(3 + 2)   # addition(+)
# print(3 - 2)   # subtraction(-)
# print(3 * 2)   # multiplication(*)
# print(3 / 2)   # division(/)
# print(3 ** 2)  # exponential(**)
# print(3 % 2)   # modulus(%)
# print(3 // 2)  # Floor division operator(//)

# # Checking data types

# print(type(10))                  # Int
# print(type(3.14))                # Float
# print(type(1 + 3j))              # Complex
# print(type('Asabeneh'))          # String
# print(type([1, 2, 3]))           # List
# print(type({'name': 'Asabeneh'}))  # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Tuple

import math
import pandas as pd

print(3+4) #addition
print(3-4) #subtraction
print(3*4) #multiplication
print(3%4) #modulus
print(3/4) #division
print(3**4) #exponential
print(3//4) #floor division

print('My name is James')
print('My family name is Mahan')
print('I live in the USA')
print('I am enjoying 30 days of Python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(9.8))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('James'))
print(type('Mahan'))
print(type('USA'))

i_number = 1
f_number = 3.4
c_number = 4+4j
s_string = 'Echo Park'
b_boolean = True
l_list = ['James', 'Cameron', 'Mahan']
t_tuple = (1, 3, 'Five', 9, False)
d_dictionary = {'Name': "James", 'City': 'Los Angeles', 'Age': "Nunya"}
s_set = (2, 4, 6, 0, 1)

print(f'this is an integer: {i_number}')
print(f'This is a float: {f_number}')
print(f'This is a complex number: {c_number}')
print(f'This is a string: {s_string}')
print(f'This is a boolean: {b_boolean}')
print(f'This is a list: {l_list}')
print(f'This is a tuple: {t_tuple}')
print(f'This is a dictionary: {d_dictionary}')
print(f'This is a set: {s_set}')

#to calculate euclidean distance, the distance between points p and q is the square root of ((p1 - q1)*2 + (p2 +q2)*2)

# p = (2,3)
# q = (10,8)

initial_calc = ((2 - 10)**2 + (3-8)**2)
final_number = math.sqrt(initial_calc)
final_number = round(final_number, 2)
print(f'The Euclidean Distance between (2,3) and (10,8) is {final_number}')
