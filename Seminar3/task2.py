# 2. Задайте список. Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.

my_list = ['2', 'fsd', '4fds']

num = input('Insert your number: ')

for elem in my_list:
    if num in elem:
        print(True)
        break
else:
    print(False)
