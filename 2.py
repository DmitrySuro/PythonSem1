# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


m = []
for i in range(5):
    m.append(int(input('Введите число')))

print(m)

print(max(m))