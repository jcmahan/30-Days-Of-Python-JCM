#iterate from 1-10 using a for loop and a while loop
print('1 - 10 using a for loop')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
print('\n1 to 10 using a while loop')
count = 0
while count < 11:
    print(count)
    count +=1
#iterate from 10-1 using a for and a while loop
print('10-1 using a for loop')
reverse_numbers = [10,9,8,7,6,5,4,3,2,1]
for number in reverse_numbers:
    print(number)
print('\n10-1 using a while loop')
count = 10
while count != 0:
    print(count)
    count -=1
print('\nPrint a triangle of #s using a loop')
triangle = '#'
tri_count = 0
while tri_count < 8:
    print(triangle)
    triangle = triangle + '#'
    tri_count +=1
print('\nPrint out the mulitiplication table with the numbers from 1-10 with their squares.')
num = 0
num_squared = num*num
while num <=10:
    print(f'{num} x {num} = {num_squared}')
    num +=1
    num_squared = num*num

print('Iterate through a list and print each item')
list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in list:
    print(item)

print('use a loop to iterate 1-100 printing only even numbers')
num = 0
while num <= 100:
    num +=1
    if num%2 == 0:
        print(num)
print('use for loop to iterate 1-100, printing only odds')
r1 = 1
r2 = 100
li = [i for i in range(r1, r2)]
for number in li:
    if number%2 == 1:
        print(number)

print('Use for loop to iterate from 0 to 100 and print the sum of all numbers.')
sum = 0
sum_even = 0
sum_odd = 0
t1 = 1
t2 = 101
t_li = [i for i in range(t1, t2)]
for number in t_li:
    sum += number
    if number%2 ==0:
        sum_even += number
    elif number%2 ==1:
        sum_odd += number
print(f'\nThe sum of all the numbers is {sum}')
print(f'\nThe sum of the even numbers is {sum_even}')
print(f'\nThe sum of the odd numbers is {sum_odd}')