########################################################	
# a открытие для добавления данных
# r открытие для чтения 
# w открытие для записи данных
# w+ r+

# a = 45
# text = ['one', 'two', 'three', 'four', 'five']
# text_value = open('file_lec_2.txt', 'a')
# text_value.writelines(text)
# text_value.write(f'\ntext {a}')
# text_value.close()
# exit()
#########################################################

# with open('file_lec_2.txt', 'w') as text_value:
# 	text_value.write('line 0\n')
# 	text_value.write('line 1\n')

#########################################################

# test = []
# path = 'file_lec_2.txt'
# text_value = open(path, 'r')
# for line in text_value:
# 	test.append(line)
# text_value.close()
# print(test)

##########################################################

# import lection_1 as lec_1

# lec_1.name(5)

########################################################## 

# def defaul_value(sym, count = 1): # присвоение значения по умолчанию для count
# 	return sym * count

##########################################################
# test_lst = []
# def  concaten(lst, *params):
# 	for item in params:
# 		lst.append(item)
# 	return lst

# print(concaten(test_lst,'23','34123', '1234123', '1324123'))

# def concaten_2(*params):
# 	res: str = "" # переменная  рес с указанием типа
# 	for item in params:
# 		res += item
# 	return res	
# print(concaten_2('3213', '12312k', '3124321,534531,1324123,5134123,23413413'))	

###########################################################
################# рекурсия ################################
###########################################################

# def  fib(n):
# 	if n in [1, 2]:
# 		return 1
# 	else:
# 		return fib(n - 1) + fib(n - 2)

###########################################################		
############## кортежи (tuple) ############################
###########################################################

# a, b = 3, 5 # множественное присваивание
# a = tuple # пустой кортеж
# a = (3, 5, 't', 343, True) # a это уже кортеж, неизменяемый список
# d = (1,) # tuple with one element
# b =[34, 45, 52, 63]
# c = tuple(b)

# print(type(a))
# print(type(b))
# print(type(c))
# print(a[3])
# print(a[-1])

# for  i in a:
# 	print(i)

########################################################### неупорядоченные  коллекции произвольных 
############ словари (dictionary) ######################### объектов с доступом по ключу 
###########################################################

# dct = {}
# dct[0] = 0
# dct[1] = 1
# dct[11] = 11 
# print(dct.keys())
# print(dct.values())
# print(dct.items()) # пары (key: value)
# print(dct)
# print(dct[0])
# print(dct.get(1))
# print(dct.get(10), 'такого ключа нет')
# dct.pop(11)
# print(dct)

# dict_ = {}
# dict_1 = \
#     {
#         'up': 'вверх',
#         'down': 'вниз',		
#         'left': 'лево'
#     }
# # print(dict_1)
# # print(dict_1['up'])

# for k in dict_1.keys(): # по ключу
# 	print(k)

# for i in dict_1.values(): # по значению
# 	print(i)


# for j in dict_1: # по индексу
#     print(dict_1[j])	

# dict_1['up'] = 'up !'
# print(dict_1['up'])


###################################################################
################### множества (set) ###############################
###################################################################

rgb = {'red', 'green', 'blue'}
# print(type(rgb)) # <class 'set'>
# rgb.add(345)
# for i in range(10):
# 	print(rgb) # {'blue', 'green', 'red'
# print(rgb) # {345, 'blue', 'green', 'red'}
# rgb.remove(345)
# print(rgb) # {'blue', 'green', 'red'}
# rgb.discard('не существующее значение')
# rgb.clear()

# f = frozenset(rgb)
# # eee = frozenset{12, 54, 56, 34, 87}
# print(type(f))

#######################################################################

# lst = [1, 2, 3, 4, 5]
# print(lst)            # [1, 2, 3, 4, 5]
# lst.pop()			  
# print(lst)            # [1, 2, 3, 4] 
# lst.pop(0)             
# print(lst)            # [2, 3, 4]  
# lst.insert(0, 1)
# print(lst)            # [1, 2, 3, 4]
# lst.append(5)
# print(lst)            # [1, 2, 3, 4, 5]

########################################################################

# 1.напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет.

a = ['asdf', 'dfds', '343566', 'adsfdre234', 'dfioad9879', 'asdf', 'asdfasd', 'asd', '54345', '234']


def first_task(lst_, str_, pos):
	print(lst_)
	lst_positions = []
	for i in range(len(lst_) - 1):
		if lst_[i] == str_:
			lst_positions.append(i)
	if len(lst_positions) < pos:
		print('вхождения нет')
		return -1
	else:
		print(lst_positions[pos - 1])
		return lst_positions[pos - 1]
		
	    	
# first_task(a, 'asdf', 2)

# 2. Задайте список. Напишите программу которая определит, присутствует ли некое число в этом списке.


def second_task(lst_, numb):
	numb = str(numb)
	for i in lst_:
		if numb in i:
			if i.isdigit():
				print('yeah')

			
			

second_task(a, 234)	
