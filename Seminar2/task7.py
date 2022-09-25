#  Для натурального n создать словарь индекс-значение,
#  состоящий из элементов последовательности 3n + 1.

#     *Пример:*

#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Insert your number:'))
my_dict = []
for i in range(1, n + 1):
    my_dict.append([i, 3 * i + 1])
print(dict(my_dict))

# n = int(input("Введите число n: "))   второй вариант решения
# my_dict = {}
# for i in range(1, n):
#     my_dict = {'ID': i, 'Value': 3 * i + 1}
#     print(my_dict)
