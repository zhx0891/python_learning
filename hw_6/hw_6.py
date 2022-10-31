
 # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N 

# def second_task(N):
#     sequ = []
#     tmp = 1
#     for i in range(1, N+1):
#         tmp = tmp * i
#         sequ.append(tmp)
#     return sequ

# def optimized(N):
# 	return list([ lambda item, ind: item * (ind - 1) for ind, item in enumerate(1, N+1) if item > 1])
	

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


		
optimized_1(5, 4, 8)

	



	


