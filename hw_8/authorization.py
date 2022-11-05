def auth():
    import proxy
    import checker as check
    import start
    proxy.clean()
    login = input('Введите  логин: ')
    password = input('Введите пароль: ')
    users = [(1,'директор', 'gfhjkm', 0), (2,'boss', '123', 0)]
    for i in users:
        if login == i[1]:
            if password == i[2]:
                if i[3] == 0:
                    print('руководитель')
                elif i[3] == 1:
                    print('водитель')
                elif i[3] == 1:
                    print('клиент')
            else:
                print('не правильный пароль')
                auth()

    choice = input('Такого пользователя нет. Чтобы попробовать снова  нажмите 1, чтобы вернуться на главную  нажмите 2,\n'
                   ' либо нажмите что угодно чтобы выйти: ')
    choice = check.check_action(choice, 1, 2, quit, quit)
    if choice == 1:
        auth()
    elif choice == 2:
        start.action_choice()
    else:
        quit()









