def check_action(choice, min, max, action):
    if choice.isdigit():
        choice = int(choice)
        if choice < min or choice > max:
            print(f'\n Одно дейсие  за раз, варианты от {min} до {max}')
            action()
        else:
            return choice
    else:
        action()