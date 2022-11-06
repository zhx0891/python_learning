import checker as check

def action_choice():
    import authorization as au
    import registration as reg


    print(f'Коллектив компании "TrueLogistik" приветствует вас \n\n 1. Авторизация. \n 2. Новый клиент. \n 3. Выход.\n\n'
          f'Выберите номер действия  и нажмите ENTER  ')
    choice = check.check_action(input('\nдействие №:'), 1, 3, action_choice, action_choice)
    if choice == 1:
        au.auth()
    elif choice == 2:
        reg.new_user()
        input('Поздравляем, теперь вы наш клиент. Авторизуйтесь и оставте  заявку. Жмите Enter.')
        au.auth()

    elif choice == 3:
        print('Будем рады видеть вас снова !!! ')
        quit()



action_choice()


