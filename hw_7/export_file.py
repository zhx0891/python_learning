
def doit():
    import proxy as pro
    import exp_html as to_html
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
            print('TXT')
            with open('txt_book.txt', 'w', encoding='utf-8') as book:
                book.write(buff)
            pro.itswork()

        elif choice == 2:
            print('HTML')
            to_html.do_html(buff)
            pro.itswork()
        elif choice == 3:
            print('CSV')
            pro.itswork()

    else:
        print('Только  цифры !!!')
        pro.dontwork()