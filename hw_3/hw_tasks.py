# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def first_task():
    sum = 0
    this_list = [23, 45, 27, 67, 40, 97]
    for i in  range(1, len(this_list), 2):
        sum = sum + this_list[i]

    print(sum)
