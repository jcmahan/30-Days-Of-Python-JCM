# Declare a function addtwonumbers. It takes two parameters and it returns a sum.

def add_two_numbers(x,y):
    result = x+y
    return result

print(f'The result of the add_two_numbers function with inputs of 5 and 10 is: {add_two_numbers(5, 10)}')

# Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates areaofcircle.
def area_of_circle(r):
    pi = 3.1416
    area = pi * r * r
    return area
print(f'The area of a circle with radius of 5 is {area_of_circle(5)}')

# Write a function called addallnums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num,(float, int)):
            print(f'The function cannot run because {num} is not a number')
            return None
        else:
            total += num
    return total
print(f'This is a successful run of the add_all_nums function, args = 1,2,3,4,5: {add_all_nums(1, 2, 3, 4, 5)}')
print(f'This is an unsuccessful run with an argument of x: {add_all_nums('x')}')

    # Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convertcelsiusto-fahrenheit.
def convert_C_to_F(c):
    fahrenheit = (c * (9/5)) + 32
    return(fahrenheit)

# print(f'The converted value of {c}°C is {fahrenheit}°F')
print(f'The converted value of 15°C to fahrenheit is: {convert_C_to_F(15)}°F')
print(f'The converted value of 10°C to fahrenheit is: {convert_C_to_F(10)}°F')
print(f'The converted value of 7°C to fahrenheit is: {convert_C_to_F(7)}°F')
print(f'The converted value of 5°C to fahrenheit is: {convert_C_to_F(5)}°F')

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['December', 'January', 'February']:
        print(f'{month} is in Winter')
    elif month in ['March', 'April', 'May']:
        return print(f'{month} is in Spring')
    elif month in ['June', 'July', 'August']:
        return print(f'{month} is in Summer')
    else:  
        return print(f'{month} is in Autumn')
print(check_season('January'))
print(check_season('April'))
print(check_season('August'))
print(check_season('November'))

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1)/(x2-x1)
    return slope

print(f'The slope of a line with coordinates (1,5) and (2,15) is: {calculate_slope(1,5,2,15)}')
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solvequadraticeqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list, *item):
    print(list)
    for item in list:
        print (item)
print(print_list(['apple', 'orange', 'banana', 'cherry', 'lime']))
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).