# . Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

num = int(input('Insert your number: '))

for i in range(0,num):
    if num%2 == 1:
        num = num*3 +1
    else:
        num = num * 7 -3
    print(num)

