#  В файле находится N натуральных чисел,
#   записанных через пробел. Среди чисел не хватает
#   одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#   Найдите это число.

my_string = '1 2 3 4 5 7 8 9'

my_list = list(map(int, my_string.split()))
for i in range(1,len(my_list)):
    if my_list[i] - my_list[i - 1] > 1:
        print(my_list[i] -1)
    
