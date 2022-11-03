def do_html(file):
	import menu
	with open('html_book.html', 'w', encoding='utf-8') as book:
		book.write('style ="font-size: 24px;"')
		book.write('<html>\n<head></head>\n<body>\n')
		book.write(f'<p> {file} </p>')
		book.write('</body>\n</html>')

	menu.action_choice()