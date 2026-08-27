# Create an empty dictionary called dog
dog = {}
print(f'The dictioary dog is: {dog}')
# Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Frankie', 'color': "grey", 'breed': 'Am Staff German Shepherd', 'legs': 4, 'age': '8 months'}
print(f'The updated dog dictionary is: {dog}')
# Create a student dictionary and add firstname, lastname, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'firstname': 'James', 'lastname': "Mahan", 'gender': 'M', 'age': 42, 'marital_status': 'married', 'skills': ['project management', 'SQL', 'Python'], 'country': 'USA', 'city': 'Los Angeles', 'address': '1355 Elysian Park Dr'}
print(f'The student dictionary is: {student}')
# Get the length of the student dictionary
print('The length of the student dictionary is', + len(student))
# Get the value of skills and check the data type, it should be a list
print(f'The skills contained in the student dictionary are {student['skills']}')
print('The length of the skills element is: ', len(student['skills']))
print('The type of the skills element is', type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('AWS')
student['skills'].extend(['Git', 'Markdown'])
print(f"The updated student's skills are {student['skills']}")
# Get the dictionary keys as a list
print('The keys of this dictionary are' , student.keys())
# Get the dictionary values as a list
print('The values contained in this dictionary are', student.values())
# Change the dictionary to a list of tuples using items() method
print(dog.values())
# Delete one of the items in the dictionary
del student['age']
print(f'The updated student dictionary is {student}')
# Delete one of the dictionaries
del student
# print(student)
