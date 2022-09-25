# 1. Напишите программу, которая принимает на вход
# число N и выдаёт последовательность из N членов.

#     *Пример:*

#     - Для N = 5: 1, -3, 9, -27, 81

# from random import random, choises

# for _ in range(int(input('введите число: '))):
#     print(randint(0, 100), end=' ')




import random


def myRandom(n):
    b = []
    for _ in range(n):
        b.append(random.randint(0, 100))
    return b


n = int(input('Insert your number'))
print(myRandom(n))
