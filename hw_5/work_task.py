from random import randint

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""
def first():
	list_task = 'Напишите программу удалабвяющую из текстаабв все слоабвва, содержаабвщие ""абв""'
	list_sp = list(list_task.split())
	result = []

	for i in list_sp:
		e = 0
		for j in range(len(i)-1):
			if i[j] == 'а' and (i[j+1] == 'б') and (i[j+2] == 'в'):
				e = 1
		if e != 1:
			result.append(i)

	print(result)


# 2. Создайте программу для игры в конфеты человек против человека.


def second():
	bunch_of_sweets = 202

	count = randint(1, 3)

	while bunch_of_sweets > 0:
		if count % 2 != 0:
			last_move = 'player_1'
			print(last_move)
			take = int(input('?'))
			if take <= 28:
				bunch_of_sweets -= take
				count += 1
				print(bunch_of_sweets)

			else:
				print('не больше 28')

		else:
			last_move = 'player_2'
			print(last_move)
			take = randint(1, 29)
			if take <= 28:
				bunch_of_sweets -= take
				count += 1
				print(bunch_of_sweets)
			else:
				print('не больше 28')

	print(f'{last_move} winner')



# 3. Создайте программу для игры в ""Крестики-нолики"".

def third():
	count = randint(1, 3)

	field = [['.', '.', '.'],
			 ['.', '.', '.'],
			 [ '.', '.', '.']]

	show_field(field)
	move(field, count)



def move(f, count):
	if count % 2 != 0:
		print('играют крестики')
	else:
		print('играют нолики')
	x = int(input('по горизонтали ?'))
	y = int(input('по вертикали ?'))
	if count % 2 != 0:
		f[x-1][y-1] = 'x'
	else:
		f[x-1][y-1] = '0'
	show_field(f)
	count += 1
	move(f, count)





def show_field(f):
	for i in f:
		print(i)













