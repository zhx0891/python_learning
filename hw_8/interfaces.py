import checker as check
import proxy as pro
import db

def boss(login = 'boss'):
    import registration as reg
    choice = input(f'Здравствуйте {login}\n\n  1. Смотреть заказы.\n  2. Смотреть маршруты.\n  3. Смотреть водителей.\n'
                   f'  4. Добавить водителя.\n  5. Выйти\n\nВаш выбор: ')
    choice = check.check_action(choice, 1, 5, boss, boss, login)
    if choice == 1:
        print('Смотреть заказы.\n\n')
        db.view_orders_drivers()
        ok()
        boss(login)

    elif choice == 2:
        print('Смотреть маршруты.')
        db.read_routes()
        ok()
        boss(login)
    elif choice == 3:
        print('Смотреть водителей.\n')
        e = [list(map(lambda x: print(f'id:{x[0]} login: {x[1]}\n'),(filter(lambda i: i[3] == 1,db.readit('users')))))]
        ok()
        boss(login)

    elif choice == 4:
        print('Добавить водителя')
        reg.new_user('1')
        ok()
        boss(login)

    elif choice == 5:
        quit()



def driver(login):
    choice = input(f'Здравствуйте {login}\n\n  1. Смотреть заказы.\n  2. Смотреть маршруты.\n  3. Выход.\n\nВаш выбор: ')
    choice = check.check_action(choice, 1, 5, driver, driver,login)
    if choice == 1:
        print('Смотреть заказы.\n\n')
        max = db.view_orders_drivers()
        choice = input('Выберите заказ или нажмите Enter для отказа. Заказ: ')
        choice = check.check_action(choice, 1, max, driver, driver, login)
        db.add_route(login, choice)
        ok()
        driver(login)
    elif choice == 2:
        db.read_routes()
        ok()
        driver(login)
    elif choice == 3:
        quit()


def client(login):
    choice = input(f'Здравствуйте {login}\n\n  1. Разместить заказ.\n  2. Статус моих заказов.\n  3. Выход.\n\nВаш выбор: ')
    choice = check.check_action(choice, 1, 5, client, client, login)
    if choice == 1:
        print('Разместить заказ.')
        db.write_order(login)
        ok()
        client(login)
    elif choice == 2:
        print('Статус  заказов.')
        e = list(map(lambda y: print(f'из:  {y[2]} в: {y[3]} груз: {y[4]}  статус: {y[5]} \n'),(filter(lambda x: x[1] == login, db.read_order()))))
        ok()
        client(login)
    elif choice == 3:
        quit()

def ok():
    input('Готово. для продолжения Enter')
    pro.clean()

# driver('test')