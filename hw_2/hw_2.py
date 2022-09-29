from random import randint
# def sum_of_digit(n):
#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
def second_task(N):
    sequ =[]
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


def fourth_task(N, a, b):
    if b == N: b -= 1
    sequence = []
    for i in range(N):
        sequence.append(randint(-N, N))

    return sequence[a] * sequence[b]


# print(second_task(4))
# print(third_task(6))
# N = int(input('N?'))
# a = int(input('a?'))
# b = int(input('b?'))
# print(fourth_task(N, a, b))