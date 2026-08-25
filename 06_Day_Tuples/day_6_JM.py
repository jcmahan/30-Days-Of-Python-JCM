# Exercises: Level 1

# Create an empty tuple
empty_type = tuple()
print(f'This is the empty typle {empty_type}')
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Danielle', 'Carrie', 'Lesley')
print(f'My sisters are {sisters}')
brothers = ('Tony', 'Dan', 'Kirk', 'Spencer')
print(f'My brothers are {brothers}')
# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(f'My siblings are {siblings}')
# How many siblings do you have?
number_of_sibs = len(siblings)
print(f'I have {number_of_sibs} siblings.')
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Jim', 'Eileen')
family_members = parents + siblings
print(f"I technically can't modify a tuple so I created a new one and added the names: {family_members}")
# Exercises: Level 2

# Unpack siblings and parents from family_members
sibling_1 = siblings[0]
sibling_2 = siblings[1]
sibling_3 = siblings[2]
sibling_4 = siblings[3]
sibling_5 = siblings[4]
sibling_6 = siblings[5]
sibling_7 = siblings[6]
dad = parents[0]
mom = parents[1]
print(f'sibling 1 is {sibling_1}')
print(f'sibling 2 is {sibling_2}')
print(f'sibling 3 is {sibling_3}')
print(f'sibling 4 is {sibling_4}')
print(f'sibling 5 is {sibling_5}')
print(f'sibling 6 is {sibling_6}')
print(f'sibling 7 is {sibling_7}')
print(f'Dad is {dad}')
print(f'Mom is {mom}')
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called foodstufftp.
fruits = tuple()
vegetables = tuple()
animal_produts = tuple()
fruits = ('apple', 'orange', 'banana')
vegetables = ('broccoli', 'cauliflower', 'green beans')
animal_produts = ('chicken breasts', 'salmon', 'ground beef')
print(f'The contents of the fruits tuple is {fruits}')
print(f'The contents of the vegetables tuple is {vegetables}')
print(f'The contents of the animal products tuple is {animal_produts}')
foodstuff = fruits + vegetables + animal_produts
print(f'The foodstuffs tuple contains {foodstuff}')
# Change the about foodstufftp tuple to a foodstufflt list
foodstuff_list = list(foodstuff)
print(f'The foodstuff list is {foodstuff_list}')
# Slice out the middle item or items from the foodstufftp tuple or foodstufflt list.
middle = foodstuff[3:6]
print(f'The middle values in the foodstuff tuple are {middle}')
# Slice out the first three items and the last three items from foodstufflt list

# Delete the foodstufftp tuple completely
del foodstuff

# Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Is Estonia a Nordic country?", 'Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Is Iceland a Nordic country?", 'Iceland' in nordic_countries)

