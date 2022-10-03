
# Работа с файлами 
# a - open for add data
# r - open for read data
# w - open for write data
# w+, r+

# dataset = ['erwqe', 'asdfsd', 'fdfasd', 'dafad']
# data = open('file.txt', 'w')
# data.writelines(dataset)
# data.write('\n text \n')
# data.close()

# with open ('file.txt', 'a') as data:
# 	data.write('text\n')
# 	data.write('text also\n')
	
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# 	print(line)
# data.close()

# exit()	


# Добавляем внешнюю функцию.
# import filepywithfunction as f

# f.nameoffunction(arg)

# def new_line(symb, count=5) # здесь указано значение по умолчанию для второго аргумента

# new_line('text' ) # Можно вызвать  только  с первым аргументом

# def concatenation(*params, nt) # здесь символ * позволяет передать несколько параметров как  первый


# Кортежи это не  изменяемые списки.Можно перебирать фориком. 
a = (3, 6, 56)
print(a) # не выведет
print(a[1]) # 6
print(a[-1]) #56

t =tuple(['red', 'green', 'blue']) # создаём список t, конвертируем его в кортеж tuple
red, green, blue = t # распаковываем кортеж 
print('r:{} g:{} b:{}'.format(red, green, blue)) # и превращаем в три переменных
