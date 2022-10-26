######################################### lambda ######################################
# Lambda аргументы: выражение

# def mylt(a, b):
# 	return a * b


# m = mylt


# def calc(a, b):
# 	return a + b


# c = calc


# def math(op, a, b):
# 	return op(a, b)


# print(math(c, 5, 6)) # 11
# print(math(m, 5, 6)) # 30

# sum = lambda x, y: x + y
# print(math(sum, 4, 5)) # 9

# print(math(lambda x, y: x ** y, 5, 3)) # 125
# max_number = lambda a, b: a if a > b else b
# print(max_number(3, 5))

# e = list([lambda i: i * 10 for i in range(1, 11)])
# print(e)
# lst_ = [12, 32, 45, 64, 53, 93, 123]
# exp = list(map(lambda x: x * 2, lst_))
# print(lst_)



############################ list comprehension #############################

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

#############################################################################
# [exp for item in iterable]
# lst_ = []
# for i in range(50):
# 		lst_.append(i)

# # print(lst_)	

# lst_exp = [i for i in range(1,50)]
# # print(lst_exp)

##############################################################################
# [exp for item in iterable (if conditional)]

# lst_ = []
# for i in range(20):
# 	if i % 2 != 0:
# 		lst_.append(i)

# print(lst_)	# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# lst_exp = [i for i in range(20) if i % 2 != 0]
# print(lst_exp) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


###############################################################################

# tuples = [(i, i) for i in range(15) if i % 2 != 0]  # создаём кортеж
# print(tuples) # [(1, 1), (3, 3), (5, 5), (7, 7), (9, 9), (11, 11), (13, 13)]

###############################################################################

# def sqrt_(e):
# 	return e ** 2

# exp_1 = [sqrt_(i) for i in range(10) if i % 2 != 0]
# print(exp_1)

###############################################################################

# exp_2 = [i ** 3 for i in range(10) if i % 2 != 0]
# print(exp_2)

# exp_3 = [(i, sqrt_(i)) for i in range(10) if i % 2 != 0]
# print(exp_3)

##############################################################################

# def conv(f, col):
# 	return[f(i) for i in col]

# def doit(f, col):
# 	return[i for i in col if f(i)]

# data = '1 3 2 4 5 6 7 2 1 9'.split()
# data = conv(int, data)
# # data = doit(lambda i: i % 2 != 0, data)
# data = doit(lambda i: not i % 2, data) 
# data = list(doit(lambda i: (i, i ** 2), data))

# print(data)


##################################################################################
########################### map ##################################################

# le = [ i for i in range(20)]
# le = list(map(lambda i: i + 10, le)) 
# # print(le)

# data = list(map(int, input('').split()))
# print(data)
# print(le)

#################################################################################
######################## seminar 5 ##############################################
#################################################################################

# def f(a=None):
# 	if a is None:
# 		a = []
# 	a.append(len(a))	
# 	return a
# print(f())

a = [(1, 2), (3, 4), (3, 6), (-1, 3), (5, 6)]
# print(max(a)) # сравнивает по первому элементу
print(max(a, key=lambda x: len(x))) # сравнивает по длинне
print(max(a, key=lambda x: x[1]) # сравнивает по второму элементу
