# . Задайте два числа. Напишите программу, которая
# найдёт НОК (наименьшее общее кратное) этих двух чисел.

num_1 = int(input('Insert first number: '))
num_2 = int(input('Inser second number: '))
i = max(num_1,num_2)

while (i % num_1 != 0 or i % num_2 != 0):

    i += 1
print(i)


# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))    
# i = max(num_1, num_2)
    
# while not (i % num_1 == 0 and i % num_2 == 0):
#     print(i % num_1)
#     print(i % num_2)
#     i += max(num_1, num_2)
# print(i)
