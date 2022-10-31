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
	

 	 
print(optimized_2('675'))
# first_task()
 	   

	



	


