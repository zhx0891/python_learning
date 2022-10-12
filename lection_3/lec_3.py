# def mat(op, x, y):
#     print(op(x, y)) 

# def sum(x, y):
# 	return x + y

# f = sum

# mat(f, 89, 45)	

#####################

# def  calc(x):
# 	return x * 10

# mat(calc, 10)


########################

# def calc(op, a, b):
# 	print(op(a, b))


# calc(lambda x, y: x + y, 4, 5)



# List comprehension
 # [exp for item in iterable]
 # [exp for item in iterable (if conditional)]  
 # [exp <if conditional> for item in iterable(if conditional)]


# lst = [i for i in range(1, 21) if i % 2 == 0]
# print(lst)

def m(x):
   return x**3

# lst = [m(i) for i in range(1, 21) if i % 2 == 0]
# print(lst)

# list_cortege = [(i, m(i)) for i in range(1,21) if i % 2 == 0] # список кортежей
# print(list_cortege) # выводит список кортежей из числа и его куба

# task_1
# with open(f'task1.txt', 'r', encoding='utf-8') as f:
#         one = f.read()
# ones = [(i, m(i)) for int(i) in one if i % 2 == 0]
# print(ones)
# one = one.split(' ')
# print(type(one))
###########################################
f = open('task1.txt', 'r')
data = f.read() + ' '
f.close()  

nums = []

while data != '': # прогон по строке пока она не пустая
    space_pos = data.index(' ') # первая позиция пробела
	nums.append(int(data[:space_pos])) # взять всё что находится от 
	# первого символа до позиции первого пробела и превратить в инт
	data = data[space_pos+1]

out = []

for e in nums:
	if not e % 2:
		out.append((e,e **2))
print(out)

	



 