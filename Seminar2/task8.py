# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

from itertools import count
from turtle import position


text1 = input('Insert your first string')
text2 = input('Insert your second string')
count = 0
position = 0
while position != -1:
    position = text1.find(text2, position)
    if position != -1:
        count += 1
print(text1,text2,count)
