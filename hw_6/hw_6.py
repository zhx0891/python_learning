# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на позициях a и b.


# def fourth_task(N, a, b):
#     if b == N: b -= 1
#     sequence = []
#     for i in range(N, 0, -1):
#         sequence.append(i * (-1))
#     for i in range(N + 1):
#         sequence.append(i)
#     print(sequence)
#     print(f' a = {sequence[a]}  b = {sequence[b]} ')
#     return sequence[a] * sequence[b]


def optimized_1(N, a, b):
	sequ = [i for i in range(-N, N)]
	print(sequ[a] * sequ[b])
	

# optimized_1(5, 4, 8)


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


# def first_task():
#     num = input('? ')
#     sum_ = 0
#     for i in num:
#        try:
#            tmp = int(i)
#            sum_ = sum_ + tmp
#        except:
#            sum_ += 0

#     return sum_


def optimized_2(N):
	lst_ = [i for i in N]
	num = list(map(int, lst_))
	sum = 0
	for i in num:
		sum += i
	return sum
	
 
# print(optimized_2('675'))

 	   
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# def second_task():
#     sec_list = [12, 34, 56, 78, 90, 98, 76, 54, 32, 1]
#     half = int(len(sec_list) / 2)
#     for i in range(half):
#         print(f' {sec_list[i]} * {sec_list[(len(sec_list) - 1) - i]} = {sec_list[i] * sec_list[(len(sec_list) - 1) - i]}')
	

def optimized_3():
	exp_list = [12, 34, 56, 78, 90, 98, 76, 54, 32, 1]
	return [exp_list[i] * exp_list[(len(exp_list) - 1) - i] for i in range(len(exp_list) // 2)]
	

# print(optimized_3())	


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# def third_task():
#     third_list = [12.5, 34.09, 56.75, 78.28, 90.61, 98.4, 76.5, 54.9, 32.21, 1.81]
#     min = third_list[0]
#     max = 0

#     for i in third_list:
#         i_str = str(i)
#         i_str_spl = i_str.split('.')
#         i_float = float(i) - float(i_str_spl[0])
#         if i_float > max:
#             max = i_float
#         if i_float < min:
#             min = i_float

#     print(f'max = {round(max, 2)}  min = {round(min, 2)} разница равна {round(max - min, 3)} ')


def optimized_4():
    third_list = [12.5, 34.09, 56.75, 78.28, 90.61, 98.4, 76.5, 54.9, 32.21, 1.81]
    lst_map = [third_list[i] - float(item[0]) for i, item in enumerate(tuple(i.split('.')) for i in list(map(str, third_list)))]
    lst_map.sort()
    return lst_map[len(lst_map) - 1] - lst_map[0]



# print(optimized_4())
    






	


