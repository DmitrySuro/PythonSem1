# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения

#     2) с помощью дополнительных библиотек Python

import math

a = int(input('Введите переменную а: '))
b = int(input('Введите переменную b: '))
c = int(input('Введите переменную c: '))
d = b**2 - 4 * a * c
if a == 0:
    x = -c / b
if d > 0:
    x_1 = (-b + math.sqrt(d))/(2*a)
    x_2 = (-b - math.sqrt(d))/(2*a)
    print(x_1, x_2)
elif d == 0:
    print('Уравнение имеет один корень')
    x = -b/(2*a)
    print(x)
else:
    print('нет корней')

# x = Symbol('x')
# y = Symbol('y')
# # x = -1.038
# # y = 3**0.5
# t = (2*x + 3*y)**2 - 3*x*(4/3*x+4*y)
# simplify(t)
# f = 4*x**4-65*x**2+16
# solve(f)
# print(f)
# Математическая библиотека Python SymPy
# https://pythonru.com/biblioteki/sympy-v-python
