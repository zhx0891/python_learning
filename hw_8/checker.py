def check_action(choice, min, max, action, action2, login ='anonymous'):
    if choice.isdigit():
        choice = int(choice)
        if choice < min or choice > max:
            print(f'\n Одно действие  за раз, варианты от {min} до {max}')
            action(login)
        else:
            return choice
    else:
        action2(login)

def test():
    print('!!')

