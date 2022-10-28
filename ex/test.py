
# num_1 = [1, 2, 3]
# print(id(num_1))
# res = num_1.copy()
# print(id(res))

# print(res)


f = [['.', '.', '0'],
	 ['.', '0', '.'],
	 ['0', '.', '0']]

# print(len(f))
# print(f[0][0])


def check_win(f, pl):
	for i in f:
		if i[0] == pl and i[1] == pl and i[2] == pl:
			print('игра окончена')
			quit()
	else:
		print("it's work")

	for	i in range(3):
		if (f[0][i]) == pl and (f[1][i]) == pl  and (f[2][i])  == pl:
			print('игра окончена')
			quit()
	else:
		print("it's work")

	
	
	if (f[0][0]) == pl and (f[1][1]) == pl  and (f[2][2])  == pl:
		print('игра окончена')
		quit()
	else:
		print("it's work")

	
	if (f[2][0]) == pl and (f[1][1]) == pl  and (f[0][2])  == pl:
		print('игра окончена')
		quit()
	else:
		print("it's work")	





check_win(f, '0')					
