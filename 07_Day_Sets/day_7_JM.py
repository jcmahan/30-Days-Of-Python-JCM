it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies
print('The length of the it_companies set is', len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f'The updated list of IT Companies is {it_companies}')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Netflix', 'Airbnb', 'Salesforce'])
print(f'Adding three companies to the list: {it_companies}')
# Remove one of the companies from the set it_companies
it_companies.remove('Salesforce')
print(f'The list after removing Salesforce: {it_companies}')

# Exercises: Level 2

# Join A and B
joined_set = A.union(B)
print(f'Sets A and B joined: {joined_set}')
# Find A intersection B
print('The intersection of A and B is', A.intersection(B))
# Is A subset of B
print('Is A a subset of B?', A.issubset(B))
# Are A and B disjoint sets
print('Are A and B disjoint sets?', A.isdisjoint(B))
# Join A with B and B with A
BtoA = A.union(B)
AtoB = B.union(A)
print(f'Joining A to B gives us {BtoA}')
print(f'Joining B to A gives us {AtoB}')
# What is the symmetric difference between A and B
print('The symmetric difference between A and B is', A.symmetric_difference(B))
# Delete the sets completely
del A
del B
# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print('The length of the age list is', len(age), 'while the length of the age set is ', len(age_set))
