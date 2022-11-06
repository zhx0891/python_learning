import proxy as pro
import checker as check
import interfaces as inter
def error():
    choice = input(
        'Не правильный  пользователь или пароль, чтобы попробовать снова  нажмите 1, чтобы вернуться на главную  нажмите 2,\n'
        ' либо нажмите что угодно чтобы выйти:')
    choice = check.check_action(choice, 1, 2, quit, quit)
    if choice == 1:
        auth()
    elif choice == 2:
        pro.action_choice()
    else:
        quit()

def auth():
    import db as db
    authorized = 0
    pro.clean()
    login = input('Введите  логин: ')
    password = input('Введите пароль: ')
    users = db.readit('users')
    for i in users:
        if login == i[1]:
            if password == i[2]:
                authorized = 1
                if i[3] == 0:
                    pro.clean()
                    inter.boss(login)
                    break
                elif i[3] == 1:
                    inter.driver()
                    break
                elif i[3] == 2:
                    inter.client()
                    break
            else:
                error()
    if authorized == 0:
        error()





# auth()









