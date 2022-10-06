# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def first_task():
    sum = 0
    this_list = [23, 45, 27, 67, 40, 97]
    for i in  range(1, len(this_list), 2):
        sum = sum + this_list[i]

    print(sum)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def second_task():
    sec_list = [12, 34, 56, 78, 90, 98, 76, 54, 32, 1]
    half = int(len(sec_list) / 2)  # не понял почему  он решил что список флоат, подставил дружеский костылёк
    print(half)
    # for i in range(len(sec_list) / 2):
    for i in range(half):
        print(f' {sec_list[i]} * {sec_list[(len(sec_list) - 1) - i]} = {sec_list[i] * sec_list[(len(sec_list) - 1) - i]}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.


def third_task():
    third_list = [12.5, 34.09, 56.75, 78.28, 90.61, 98.4, 76.5, 54.9, 32.21, 1.81]
    min = 0
    max = 0

    for i in third_list:
        r = False
        i_str = str(i)
        i_str_spl = i_str.split('.')
        zero_ahead = i_str_spl[1].split()

        if (r):
            print(f'i_str = {float(i_str)}  i_str_spl = {float(i_str_spl[0])}')
            i_float = float(i_str) - float(i_str_spl[0])
        else:
            i_float = float(i_str_spl[1])

        # print(i_float)
    #     if i_float > max:
    #         max = i_float
    #     if i_float < min:
    #         min = i_float
    #
    # print(f'max = {max}  min = {min} ')



