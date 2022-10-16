#  Напишите программу вычисления арифметического выражения заданного строкой.
#   Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:*
#         1+2*3 => 7;
#         (1+2)*3 => 9;

def my_action(op, digit_1, digit_2):
    if op == '+':
        return digit_1 + digit_2
    elif op == '-':
        return digit_1 - digit_2
    elif op == '/':
        return digit_1 // digit_2
    elif op == '*':
        return digit_1 * digit_2


def brackets(my_string):
    my_list_symbols = [i for i in my_string if not i.isdigit()]
    my_list_digits = [int(i) for i in my_string if i.isdigit()]
    while '*' in my_list_symbols or '/' in my_list_symbols:
        for i, e in enumerate(my_list_symbols):
            if e in ('*', '/'):
                my_list_digits[i] = my_action(
                    e, my_list_digits[i], my_list_digits[i+1])
                del my_list_digits[i+1]
                del my_list_symbols[i]
    while len(my_list_symbols) > 0:
        for i, e in enumerate(my_list_symbols):
            my_list_digits[i] = my_action(
                e, my_list_digits[i], my_list_digits[i+1])
            del my_list_digits[i+1]
            del my_list_symbols[i]
    return str(my_list_digits[0])


my_string_out = '(1+2)+(3*5-6/3+7-9*0)*3*4'

while '(' in my_string_out:
    i_bracket_l = my_string_out.index('(')
    i_bracket_r = my_string_out.index(')')
    my_string_out = my_string_out[:i_bracket_l] + \
        brackets(my_string_out[i_bracket_l+1:i_bracket_r]) + \
        my_string_out[i_bracket_r:]
    print(my_string_out)


# print(my_list_symbols)
print(my_string_out)
