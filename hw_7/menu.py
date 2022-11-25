import import_file as imp
import export_file as exp
import view_book as see
import add_contact as new


def action_choice():
	print(f'Что будем делать? \n\n 1. Экспорт телефонной книги \n 2. Импорт телефонной книги. \n 3. Просмотр телефонной книги. \n 4. Новая запись.\n 5. Выход.\n\nВыберите номер действия  и нажмите ENTER  ')
	choice = input('\nдействие №:')
	if choice.isdigit():
		choice = int(choice)
		if choice < 1 or choice > 5:
			print('\n Одно дейсие  за раз, вариаты от 1 до 5')
			action_choice()

		elif choice == 2:
			imp.doit()
		elif choice == 1:
			exp.doit()
		elif choice == 3:
			see.doit()
		elif choice == 4:
			new.doit()
		elif choice == 5:
			quit()


	else:
		print('Только  цифры !!!')
		action_choice()


action_choice()

matr = [['. ','. ','. ','. '],
        ['. ','. ','. ','. '],
        ['. ','. ','. ','. '],
        ['. ','. ','. ','. ']]

for i in matr:
	print()
	for j in i:
		print(j, end='')
for i in matr:
	

print('\n' * 3)		