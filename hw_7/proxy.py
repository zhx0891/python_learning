
def itswork():
    import menu
    clear()
    menu.action_choice()


def dontwork():
    import menu
    clear()
    print('Ошибка ввода. Моё почтение, сэр тэстэр.')
    menu.action_choice()

def clear():
    print('\n' * 100)