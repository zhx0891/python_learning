

def doit():
    import proxy as pro
    with open('phonebook', 'r', encoding='utf-8') as book:
        print(book.read())

    input('Для продолжения нажмите Enter.')
    pro.itswork()