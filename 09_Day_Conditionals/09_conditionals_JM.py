# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

able_to_drive = int(input('Enter your age: '))
remnant = (18 - able_to_drive)
if able_to_drive > 18:
        print('You are old enough to drive.')
else: 
    print(f'You need {remnant} more years to learn to drive.')


# Compare the values of myage and yourage using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if myage = yourage. Output:

myage = int(input('Input my age: '))
yourage = int(input('Input your age: '))
difference = yourage-myage
if difference == 1:
    print('You are one year older than I am.')
elif difference == 0:
    print('We are the same age.')
elif difference > 1:
    print(f'You are {difference} years older than I am')
else:
    print('I am older than you are')

# Enter your age: 30
# You are 5 years older than me.
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:

num_a = int(input('Enter number one: '))
num_b = int(input('Enter number two: '))

if num_a > num_b:
    print(f'{num_a} is greater than {num_b}')
elif num_b > num_a:
    print(f'{num_b} is greater than {num_a}')
else:
    print(f'{num_a} is equal to {num_b}')


# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3


# Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:
grade = int(input('Enter your grade: '))
if grade >=90 and grade < 100:
    print(f'Your {grade} is equal to an A')
elif grade >=80 and grade < 90:
    print(f'Your {grade} is equal to a B')
elif grade >=70 and grade < 80:
    print(f'Your {grade} translates to a C')
elif grade >=60 and grade < 70:
    print(f'Your {grade} grants you a D')
else:
    print(f'Your {grade} denotes failure, an F')
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# month = input('Enter a month, please: ')
if month in ['December', 'January', 'February']:
    print(f"{month} is in Winter")
elif month in ['March', 'April', 'May']:
    print(f'{month} is in Spring')
elif month in ['June', 'July', 'August']:
    print(f'{month} is in Summer')
else:
    print(f'{month} is in Autumn')

# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit, please: ')
if new_fruit in fruits:
    print('That fruit already exists in the list')
elif new_fruit not in fruits:
    fruits.append(new_fruit)
    print(fruits)
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }