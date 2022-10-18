
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
red, green, blue = t # распаковываем кортеж и превращаем в три переменных
print('r:{} g:{} b:{}'.format(red, green, blue))  

#Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу
 dict_empty = {} # empty dictionary
 dict_full = \
 {'up': ' ^ ',
 'left': ' < ',
 'right': ' >'}
 print(dict_full)
 print(dict_full['up'])

for i in dict_full.keys():
	print(i)

for j in dict_full.values():
	print(j)

for j in dict_full:
	print(j)

for k in dict_full.values():
	print(dict_full[k])

print(dict_full['up'])
dict_full['up'] = 'up_'


# Множества
colors = {'yellow', 'black', 'pink'}
print(colors)
colors.add('new')
colors.remove('new')
colors.discard('new') # не вызовет исключеня если элемента нет
colors.clean() # очищает множество
new_colors = {'red', 'green', 'blue'}
u = a.union(b) # объединение множеств
i = a.intersection(b)
c = a.copy(b)
da = a.differens(b)
db = b.differens(a)


# work with lists
list1 = [1,3,5,5,4]
print(list1)
list = (list1.pop()) # delete last element
print(list1.pop(1)) # delete element with index  1
print(list1.insert(2, 11)) #вставить на вторую позицию значение 11

print(list1.append(13))