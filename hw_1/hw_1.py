# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
import math

# print('???')
# day = int(input())
# if day == 6 or day == 7:
#     print('выходной')
# else:
#     print('не выходной')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# print('введите X не равный 0')
# x = int(input())
# print('введите Y не равный 0')
# y = int(input())
# if x == 0 or y == 0: print("введёные координаты не соответствуют условиям")
# if x > 0 and y > 0: print("первая четверть")
# if x < 0 and y > 0: print("вторая  четверть")
# if x < 0 and y < 0: print("третья четверть")
# if x > 0 and y < 0: print("четвёртая четверть")

 #Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# print("введите номер четверти")
# num_quarter = int(input())
# if num_quarter == 1: print("x > 0 and y > 0")
# if num_quarter == 2: print("x < 0 and y > 0")
# if num_quarter == 3: print("x < 0 and y < 0")
# if num_quarter == 4: print("x > 0 and y < 0")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# d^2= (х2— х1)^2+ (y2— y1)^2.
# point_a = [0, 0]
# point_b = [3, 4]
# print("введите  координату Х для точки А")
# point_a[0] = int(input())
# print("введите  координату Y для точки А")
# point_a[1] = int(input())
# len_line = math.isqrt((point_b[0]-point_a[0]) ** 2 + (point_b[1]-point_a[1]) ** 2)
#
# print(len_line)

check_true = True
meaning_predicats = [1, 0, 0]
x = meaning_predicats[0]
y = meaning_predicats[1]
z = meaning_predicats[2]

check_true=(not(x or y or z)) == ((not x) and (not y) and (not z))
print(f'при x = {x}  y =  {y}  z = {z}  выражение = {check_true} ')

