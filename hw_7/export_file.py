def doit():
    import menu
    print('Как будем экспортировать?\n')
    print(' 1. TXT \n')
    print(' 2. HTML \n')
    print(' 1. CSV \n')

    choice = input('Формат:')
    if choice.isdigit():
        choice = int(choice)
        if choice < 1 or choice > 3:
            menu.action_choice()
        elif choice == 1:
            with open('phonebook', 'r', encoding='utf-8') as book:
                buff = book.read()
            with open('export_phonebook', 'w', encoding='utf-8') as book:
                book.write(buff)

        elif choice == 2:
            print('html')
        elif choice == 3:
            print('csv')

    else:
        print('Только  цифры !!!')
        menu.action_choice()