def do_html():
	with open('pattern.html', 'r', encoding='utf-8') as patt:
		buff = patt.read()
	data = []
	with open('phonebook', 'r', encoding='utf-8') as book:
		data = book.read()

	data = data.split('\n\n')
	data.pop()


	with open('html_book.html', 'w', encoding='utf-8') as exp:
		exp.write(buff)
		for i in range(len(data)):
			e = (data[i].split(' \n'))
			exp.write(f'\n <strong>{e[0]}</strong><br>')
			exp.write(f'\n <font color ="red">{e[1]}</font><br>')
			exp.write(f'\n <i>{e[2]}</i><br><br>')

		exp.write('</body>')
		exp.write('</html>')













do_html()