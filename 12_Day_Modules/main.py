
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(f'The name stemming from the imported generate_full_name function is {fullname('James','Mahan')}')
print(f'The total of 15 and 17 from the imported sum_two_nums function is {total(15, 17)}')
mass = 100
print(f'The value of mass is {mass}')
weight = mass * g
print(f'weight is equal to mass times gravity. In this case, weight is {weight}')
print(f'The person imported from the module is {p}')
print(f'The firstname of the person imported from the module is {p['firstname']}')

#import the os module
import os as os
print(os.getcwd())
#create and remove a directory
# os.mkdir('Folder from Python')
# os.rmdir('Folder from Python')
import random
import string
pool = string.ascii_letters + string.digits
def random_user_id():
    random_id = ''.join(random.choices(pool, k=6))
    return random_id
print(f'\nThe random user id created is: {random_user_id()}')

