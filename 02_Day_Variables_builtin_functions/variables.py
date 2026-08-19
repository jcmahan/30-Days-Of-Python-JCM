
# Variables in Python

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#     'firstname': 'Asabeneh',
#     'lastname': 'Yetayeh',
#     'country': 'Finland',
#     'city': 'Helsinki'
# }

# # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# # Declaring multiple variables in one line

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)
#Day 2: 30 Days of Python Programming
first_name = 'James'
last_name = 'Mahan'
full_name = 'James Mahan'
country = 'USA'
city = 'Los Angeles'
age = 52
year = 2026
is_married = True
is_true = True
is_light_on = False

first_name_1, last_name_1, full_name_1, country_1, city_1, age_1, is_married_1 = 'JR', 'Hills', 'JR Hillis', 'US', "Echo Park, CA", 43, True
print(first_name_1, last_name_1, full_name_1, country_1, city_1, age_1, is_married_1)

print(f'The type of first_name is: {type(first_name)}')
print(f'The type of last_name is: {type(last_name)}')
print(f'The type of full_name is: {type(full_name)}')
print(f'The type of country is: {type(country)}')
print(f'The type of city is: {type(city)}')
print(f'The type of age is: {type(age)}')
print(f'The type of year is: {type(year)}')
print(f'The type of is_married is: {type(is_married)}')
print(f'The type of is_true is: {type(is_true)}')
print(f'The type of is_light_on is: {type(is_light_on)}')

print(f'the length of first_name is: {len(first_name)}')
print(f'The length of last_name is: {len(last_name)}')

num_one = 5
num_two = 4
print(f'num_one is: {num_one}')
print(f'num_two is: {num_two}')
total = num_one + num_two
print(f'The sum of num_one and num_two is: {total}')
diff = num_two - num_one
print(f'The difference of num_two and num_one is: {diff}')
product = num_one * num_two
print(f'The product of num_one and num_two is: {product}')
division = num_two/num_one
print(f'The division of num_two by num_one is: {division}')
remainder = num_two%num_one
print(f'The remainder when num_two modulus num_one is: {remainder}')
exp = num_one**num_two
print(f'num_one raised to the power of num_two is: {exp}')
floor_division = num_two//num_one
print(f'The floor division of num_two by num_one is: {floor_division}')
radius = 30
pi = 3.1416
area = radius * pi
print(f'the area of a circle with a radius of {radius}m is: {area}')
circumference = 2 * pi * radius
print(f'the circumference of a circle with radius of {radius}m is: {circumference}')

new_radius = input('Input a radius please: ')
new_radius = int(new_radius)
new_area = new_radius * pi
print(f'The area of the circle with {new_radius}m is: {new_area}')

new_first_name = input('What is your first name? ')
new_last_name = input('What is your last name? ')
new_country = input('And in which country do you live? ')
new_age = input('And how old are you telling people you are? ')
print(f'This new user is {new_first_name} {new_last_name}. They live in {new_country} and are telling people they are {new_age}.')