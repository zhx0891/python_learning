import proxy
def doit():
    input('Положите ваш импортируемый файл (txt_book.txt)в каталог программы и нажмите Enter.')
    with open('txt_book.txt', 'r', encoding='utf-8') as book:
        buff = book.read()

    with open('phonebook', 'a', encoding='utf-8') as phonebook:
        phonebook.write(buff)

    input('Импорт выполнен. Enter для продолжения.')

    proxy.itswork()
