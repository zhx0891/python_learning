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
        print(f' {sec_list[i]} + {sec_list[(len(sec_list) - 1) - i]} = {sec_list[i] + sec_list[(len(sec_list) - 1) - i]}')




