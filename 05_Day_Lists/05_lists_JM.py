# Declare an empty list
empty_list = []
print(f'My list {empty_list} is empty.')
# Declare a list with more than 5 items
five_item_list = ['California', 'Hawaii', 'Washington', 'Oregon', 'Colorado']
print(f'My five item list is: {five_item_list}')
# Find the length of your list
print('The length of this list is ', len(five_item_list))
# Get the first item, the middle item and the last item of the list
print('The first item on this list is', five_item_list[0])
print('The third item on this list is', five_item_list[2])
print('The last item on this list is', five_item_list[4])

# Declare a list called mixeddatatypes, put your(name, age, height, marital status, address)
mixeddatatypes = ['James', 42, "5 foot 9", 'married', '1355 Elysian Park Dr, Los Angeles, CA 90026']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(f'The list of IT Companies is: {it_companies}')
# Print the number of companies in the list
print('The length of the IT Companies list is: ', len(it_companies))
# Print the first, middle and last company
print('The first item on the list of IT Companies is:', it_companies[0])
print('The middle item on the list of IT Companies is:', it_companies[3])
print('The last item on the list of IT Companies is:', it_companies[-1])
# Print the list after modifying one of the companies
it_companies[0] = 'Netflix'
print(f'The list of IT Companies after being modified is: {it_companies}')
# Add an IT company to it_companies
it_companies.append('LinkedIn')
print(f'The list after appending a company is: {it_companies}')
# Insert an IT company in the middle of the companies list
it_companies.insert(2, 'Airbnb')
print(f'The list of companies after inserting a company at position 3 is: {it_companies}')
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(f'The list of companies after making the third element uppercase is: {it_companies}')
# Join the it_companies with a string '#;  ', 
result = '#; '.join(it_companies)
print(result)
# Check if a certain company exists in the it_companies list.
print('Is Netflix in the list of IT Companies?', 'Netflix' in it_companies)
# Sort the list using sort() method
it_companies.sort(reverse=False)
print(f'The sorted list of IT Companies is: {it_companies}')
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(f'The sorted list of IT Companies, reversed, is: {it_companies}')
# Slice out the first 3 companies from the list
sliced_list = it_companies[0:3]
print(f'The first three items sliced from the list are: {sliced_list}')
# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(f'The last three items on the list are: {last_three}')
# Slice out the middle IT company or companies from the list
middle_company = it_companies[4:5]
print(f'The middle company in the list is: {middle_company}')
# Remove the first IT company from the list
it_companies.pop(0)
print(f'The new list without the first company is: {it_companies}')
# Remove the middle IT company or companies from the list
del it_companies[3:5]
print(f'The list of IT Companies without the middle companies is: {it_companies}')
# Remove the last IT company from the list
it_companies.pop()
print(f'The list with the last company removed is: {it_companies}')
# Remove all IT companies from the list
it_companies.clear()
print(f'The IT Companies list without anything on it is: {it_companies}')
# Destroy the IT companies list
del(it_companies)
# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(f'The full stack list of technologies is: {full_stack}')

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(4, 'Python')
print(f'The list of technologies with Python inserted is: {full_stack}')
# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'The sorted list of ages is {ages}')
min_age = min(ages)
max_age = max(ages)
print(f'The min age on the list is {min_age} and the max age is {max_age}')
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
new_ages = ages.extend([19, 26])
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
total = sum(ages)
age_length = len(ages)
mean_age = total/age_length
print(f'The average age is {mean_age}')
#
# Find the range of the ages (max minus min)
age_range = max_age - min_age
print(f'The range of the ages is: {age_range}')
# Compare the value of (min - average) and (max - average), use abs() method

min_minus = (min_age - mean_age) 
max_minus = (max_age - mean_age)
print(f'the min_age minus the mean is {min_minus} and max_age minus the mean is {max_minus}')
print(min_minus == max_minus)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Unpack the first three countries and the rest as scandic countries.
ch, ru, usa, *scandic = countries
print(ch)
print(ru)
print(usa)
print(scandic)