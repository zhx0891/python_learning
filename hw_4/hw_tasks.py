from decimal import *
import random
from math import *

getcontext().prec = 100


# 1. Вычислить число π c заданной точностью


def first_task():
    acc = input('количество знаков после запятой')
    result = Decimal(3.0)
    op = 1
    n = 2

    for n in range(2, 2 * (10 ** 5) + 1, 2):
        result += 4 / Decimal(n * (n + 1) * (n + 2) * op)
        op *= -1

    result = round(result, acc)
    print(result)






    # tmp = 0.0
    # count = 1
    # p = 0.0
    # for i in range(2, reps):
    #     p = (4 / (i * (i + 1) * (i + 2)))
    #     if count % 2 == 0:
    #         tmp = 3 + p
    #     else:
    #         tmp = 3 - p
    #     count += 1
    # print(tmp)














# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def second_task(N):
    sm = []
    for i in range(2, N):
        while(N % i) == 0:
            sm.append(i)
            N //= i

    print(sm)

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
def third_task():
    sequence = [2, 4, 4, 6, 7, 2, 9, 0, 9, 5, 3, 6, 7, 4, 1]
    unique_els = []
    for i in sequence:
        count = 0
        if(count < 2):
            for j in sequence:
                if i == j:
                    count += 1
        if count < 2:
            unique_els.append(i)
    print(unique_els)


# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

def fourth_task(file_name,k):
    liters = 'abcd'
    signs = '+-'

    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        multiple = random.randint(0, 101)
        literal = liters[random.randint(0, 3)]
        literal_two = liters[random.randint(0, 3)]
        sign = signs[random.randint(0, 1)]
        f.write(str(multiple) + literal + sign + literal_two + f'^{k}')



# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов. Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличать


def fifth_task(file_name1, file_name2):
    def work_it(ls):
        coeff = ''
        sign =''
        liter = ''

        for i in ls:
            if i.isdigit():
                coeff = coeff + i
            if i.isalpha():
                coeff_int = int(coeff)
                coeff = ''
                liter = liter + i

            if (i.isdigit() == False) or (i.isalpha() == False):
                sign = i


        print(f' коэфицент = {coeff_int}')
        print(f' литеры = {liter}')
        print(f' знак =  {sign}')


    with open(f'{file_name1}.txt', 'r', encoding='utf-8') as f:
        multip_one = f.readline()
        print(multip_one)

    with open(f'{file_name2}.txt', 'r', encoding='utf-8') as e:
        multip_two = e.readline()
        print(multip_two)

    work_it(multip_one)


    # one = {'coeff': , 'liter': 'b', 'sing': ,   }








