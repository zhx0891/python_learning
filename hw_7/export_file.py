
def doit():
    import proxy as pro
    import exp_html as to_html
    pro.clear()
    print('Как будем экспортировать?\n')
    print(' 1. TXT \n')
    print(' 2. HTML \n')
    print(' 3. CSV \n')
    with open('phonebook', 'r', encoding='utf-8') as book:
        buff = book.read()

    choice = input('Формат:')
    if choice.isdigit():
        choice = int(choice)
        if choice < 1 or choice > 3:
            pro.dontwork()
        elif choice == 1:
            with open('txt_book.txt', 'w', encoding='utf-8') as book:
                book.write(buff)

            input('Экспорт в TXT выполнен.Enter.')
            pro.itswork()

        elif choice == 2:
            to_html.do_html()
            pro.itswork()
        elif choice == 3:
            input('Экспорт в CSV не выполнен.Enter.')
            pro.itswork()

    else:
        print('Только  цифры !!!')
        pro.dontwork()