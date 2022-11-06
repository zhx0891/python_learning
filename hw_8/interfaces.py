import checker as check
import proxy as pro
import db
def boss(login = 'boss'):
    import registration as reg
    choice = input(f'Здравствуйте {login}\n\n  1. Смотреть заказы.\n  2. Смотреть маршруты.\n  3. Смотреть водителей.\n'
                   f'  4. Добавить водителя.\n  5. Выйти\n\nВаш выбор: ')
    choice = check.check_action(choice, 1, 5, boss, boss)
    if choice == 1:
        print('Смотреть заказы.')
    elif choice == 2:
        print('Смотреть маршруты.')
    elif choice == 3:
        print('Смотреть водителей.\n')
        print([list(map(lambda x: print(f'id:{x[0]} login: {x[1]}\n'),(filter(lambda i: i[3] == 1,db.readit('users')))))])
        input('Готово. для продолжения Enter')
        pro.clean()
        boss(login)

    elif choice == 4:
        print('Добавить водителя')
        reg.new_user('1')
        input('Готово. для продолжения Enter')
        pro.clean()
        boss(login)

    elif choice == 5:
        quit()



def driver(login):
    choice = input(f'Здравствуйте {login}\n\n  1. Смотреть заказы.\n  2. Взять заказ.\n  3. Мои  маршруты.\n\nВаш выбор: ')


def client(login):
    choice = input(f'Здравствуйте {login}\n\n  1. Разместить заказ.\n  2. Статус моих заказов.\n  3. Выход.\n\nВаш выбор: ')
    choice = check.check_action(choice, 1, 5, client, client)
    if choice == 1:
        print('Разместить заказ.')
        db.write_order(login)
        input('Готово. для продолжения Enter')
        pro.clean()
        client(login)
    elif choice == 2:
        print('Статус  заказов.')
        print(list(map(lambda y: print(f'из:  {y[1]} в: {y[2]} груз: {y[3]}  статус: {y[4]} \n'),(filter(lambda x: x[0] == login,db.read_order())))))
        input('Готово. для продолжения Enter')
        pro.clean()
        client(login)
    elif choice == 3:
        quit()
