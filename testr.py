def printArr(arr):
	for i in arr:
		print()
		for j in i:
			print(j, end=' ')


n = 10
lst = list([i for i in range(n)] for i in range(n))
for i in range(len(lst)):
	val = i
	if i > 0:
		act = '-'
	for j in range(len(lst)):
		if val == 0:
			act = '+'
		if act == '+':
			lst[j][i] = val
			val += 1
		else:
			lst[j][i] = val
			val -= 1
printArr(lst)

