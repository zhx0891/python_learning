from random import randint
import os

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
	cells = 0
	count = randint(1, 3)

	field = [['.', '.', '.'],
			 ['.', '.', '.'],
			 ['.', '.', '.']]

	show_field(field, cells)
	move(field, count, cells)


def gameover():
	print('игра окончена')
	quit()


def move(f, count, cells):
	if cells < 9:
		if count % 2 != 0:
			print('играют крестики')
		else:
			print('играют нолики')
		x = int(input('по вертикали?'))
		y = int(input('по горизонтали  ?'))
		cells += 1
		if count % 2 != 0:
			f[x - 1][y - 1] = 'x'
		else:
			f[x - 1][y - 1] = '0'
		show_field(f, cells)
		count += 1
		check_win(f, count)
		move(f, count, cells)
	else:
		show_field(f, cells)
		gameover()


def show_field(f, cells):
	if cells < 9:
		for i in f:
			print(i)
	else:
		for i in f:
			print(i)
		gameover()

def check_win(f, count):
	if count % 2 != 0:
		pl = 'x'
	else:
		pl = '0'

	for i in f:
		if i[0] == pl and i[1] == pl and i[2] == pl:
			gameover()

	for	i in range(3):
		if (f[0][i]) == pl and (f[1][i]) == pl  and (f[2][i])  == pl:
			gameover()

	if (f[0][0]) == pl and (f[1][1]) == pl and (f[2][2]) == pl:
		gameover()

	if (f[2][0]) == pl and (f[1][1]) == pl and (f[0][2]) == pl:
		gameover()





	# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def fourth_pack_rle(task_str):
	res = ''
	count = 0
	for ind, i in enumerate(task_str):
		if ind != (len(task_str) - 1):
			if i != task_str[ind + 1]:
				count += 1
				res += (f'{str(count)}.{i} ')
				count = 0
			else:
				count += 1
		else:
			res += (f'{str(count)}.{i} ')
	print(res)
	return res


def fourth_unpack_rle(unp):
	res = ''
	unp_sp = unp.split(' ')
	for i in unp_sp:
		a = i.split('.')
		res += (int(a[0]) * a[1])

	print(res)
	return res

# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.












