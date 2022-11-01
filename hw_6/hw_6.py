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


def first_task():
    num = input('? ')
    sum_ = 0
    for i in num:
       try:
           tmp = int(i)
           sum_ = sum_ + tmp
       except:
           sum_ += 0

    return sum_

def optimized_2(N):
	lst_ = [i for i in N]
	num = list(map(int, lst_))
	sum =0
	for i in num:
		sum += i
	return sum
	

 	 
# print(optimized_2('675'))

 	   


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def second_task():
    sec_list = [12, 34, 56, 78, 90, 98, 76, 54, 32, 1]
    half = int(len(sec_list) / 2)
    for i in range(half):
        print(f' {sec_list[i]} * {sec_list[(len(sec_list) - 1) - i]} = {sec_list[i] * sec_list[(len(sec_list) - 1) - i]}')
	


def optimized_3():
	exp_list = [12, 34, 56, 78, 90, 98, 76, 54, 32, 1]
	return [exp_list[i] * exp_list[(len(exp_list) - 1) - i] for i in range(len(exp_list) // 2)]
	


print(optimized_3())	


	


