import math
print('Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,\n является ли этот день выходным.')

print()
print('введите номер дня  недели, программа не рассчитана на хитрых тестеров')
day = int(input())
if day == 6 or day == 7:
    print('выходной')
else:
    print('не выходной')


print()
print('Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0\nи выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).')

x = int(input('введите X не равный 0'))
y = int(input('введите Y не равный 0'))

if x == 0 or y == 0: print("введёные координаты не соответствуют условиям")
if x > 0 and y > 0: print("первая четверть")
if x < 0 and y > 0: print("вторая  четверть")
if x < 0 and y < 0: print("третья четверть")
if x > 0 and y < 0: print("четвёртая четверть")


print()

print('Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных\n координат точек в этой четверти (x и y)')


print()

num_quarter = int(input("введите номер четверти"))
if num_quarter == 1: print("x > 0 and y > 0")
if num_quarter == 2: print("x < 0 and y > 0")
if num_quarter == 3: print("x < 0 and y < 0")
if num_quarter == 4: print("x > 0 and y < 0")


print()
print('Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними\nв 2D пространстве. d^2= (х2— х1)^2+ (y2— y1)^2.')


print()
point_a = [0, 0]
point_b = [3, 4]
print("введите  координату Х для точки А")
point_a[0] = int(input())
print("введите  координату Y для точки А")
point_a[1] = int(input())
len_line = math.isqrt((point_b[0]-point_a[0]) ** 2 + (point_b[1]-point_a[1]) ** 2)

print(len_line)

print()
print('Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')

print()
check_true = True
meaning_predicats = [0,1]
for x in meaning_predicats:
    for y in meaning_predicats:
        for z in meaning_predicats:
            check_true = (not (x or y or z)) == ((not x) and (not y) and (not z))
            print(f'при x = {x}  y =  {y}  z = {z}  выражение = {check_true} ')



