# a = [(7, 1, 6), (2, 4, 5), (2, 0, 8), (3, 3), (1, 2, 4, 6)]
# print(max(a))
# print(min(a))
# print(min(a, key=lambda x: len(x)))
# print(max(a, key=len))
# print(max(a, key=lambda x: x[1]))

# c = ['1', '2', '3', '6']
# print(max(c, key=int))

# list comprehension
#  a = []
#  for i in range(10):
#  	a.append(i * i)

# print(a)

# b = [i * i for i in range(11) if i % 2 == 0]
# c = [i * i if i % 2 == 0 else i ** 3 for i in range(11)]
# c = [i * i if i % 2 == 0 else i ** 3 for i in range(11) if i % 5 != 0]
# print(b)
# print(c)

############################################################
###################  map & filter  #########################
############################################################

a = [1, 2, 3, 4, 5, 6, 6]

itog = list(map(lambda x: x **2, a))
print(itog) 
filter_itog = list(filter(lambda x: x % 2 == 0, a)) 
print(filter_itog)



 
