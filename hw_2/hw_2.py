from random import randint

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def first_task():
    num = input('? ')
    sum_ = 0
    for i in num:
        # if i.isnumeric(): # не понял почему не сработало, рассчитывал что она пропустит точку
        #     sum_ += i
       try:
           tmp = int(i)
           sum_ = sum_ + tmp
       except:
           sum_ += 0

    return sum_


#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N


def second_task(N):
    sequ = []
    tmp = 1
    for i in range(1, N+1):
        tmp = tmp * i
        sequ.append(tmp)
    return sequ

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.

def third_task(n):
    ind = 0
    for i in range(1, n+1):
        ind += (1 + (1 / i)) ** i

    print(ind)
    return round(ind, 3)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.


def fourth_task():
    N = int(input('N?'))
    a = int(input('a?'))
    b = int(input('b?'))
    if b == N: b -= 1
    sequence = []
    for i in range(N):
        sequence.append(randint(-N, N))

    return sequence[a] * sequence[b]


# Реализуйте алгоритм перемешивания списка.


def fifth_task():
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(list_)-1):
        tmp = list_[i]
        ind = randint(i+1, len(list_)-1)
        list_[i] = list_[ind]
        list_[ind] = tmp

    print(list_)






# print(first_task())
# print(second_task(4))
# print(third_task(6))
# print(fourth_task())
fifth_task()