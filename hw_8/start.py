def action_choice():
    import checker as check
    import  proxy as pro
    import authorization as au
    pro.clean()
    print(f'Коллектив компании "TrueLogistik" приветствует вас \n\n 1. Авторизация. \n 2. Новый клиент. \n 3. Выход.\n\n'
          f'Выберите номер действия  и нажмите ENTER  ')
    choice = check.check_action(input('\nдействие №:'), 1, 3, action_choice, action_choice)
    if choice == 1:
        au.auth()
    elif choice == 2:
        print('регистрация')
    elif choice == 3:
        print('Будем рады видеть вас снова !!! ')
        quit()



action_choice()


