# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""
def first():
	list_task = 'Напишите программу удалабвяющую из текстаабв все слоабвва, содержаабвщие ""абв""'
	list_sp = list(list_task.split())
	result = []

	for i in list_sp:
		e = 0
		for j in range(len(i)-1):
			if i[j] == 'а' and  (i[j+1] == 'б') and (i[j+2] == 'в'):
				e = 1
		if e != 1:
			result.append(i)

	print(result)



