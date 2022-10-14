# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""
list_task = 'Напишите программу удалабвяющую из текстаабв все слоабвва, содержаабвщие ""абв""'
list_task_sp = (list_task.split())

for i in list_task_sp:
	print(i)
	for j in range(len(i)-1):
		print(i[j])
		if i[j] == 'а':
			if i[j+1] == 'б':
				if i[j+2] == 'в':
					list_task_sp.remove(i)

# print(list_task_sp)
	


