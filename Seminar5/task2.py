# . Дан список чисел. Создайте список, в который попадают числа, описываемые 
# возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    
def new_list(my_string):
    if my_string[0] == max(my_string):
        return new_list(my_string[1:])
    else:
        myList = [my_string[0]]
        for i in range(1,len(my_string)):
            if myList[-1]<my_string[i]:
                myList.append(my_string[i])
        return myList


my_string_1 = [9, 1, 5, 2, 3, 4, 6, 1, 7]

print(new_list(my_string_1))
