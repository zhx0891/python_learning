def only_digit(tmp):
    digit = ''
    for i in tmp:
        if i.isdigit():
            digit += i
    return int(digit)


def calc(str_):
    str_spl = str_.split()
    print(len(str_spl))
    if len(str_spl) < 4:
        if str_spl[0].isdigit() and str_spl[2].isdigit():
            a = int(str_spl[0])
            b = int(str_spl[2])
            action = str_spl[1]
            if action == '+':
                print(f"{a} + {b} = {a + b}")
            elif action == '-':
                print(f"{a} - {b} = {a - b}")
            elif action == '*':
                print(f"{a} * {b} = {a * b}")
            elif action == '/':
                print(f"{a} / {b} = {a / b}")
            else:
                print('некорректное действие')
        else:
            print("Некорректный ввод")
    else:
        print('complex_calc')
        # complex_calc(str_spl)


def complex_calc(lst_):
    if len(lst_) == 7:
        if(((lst_[0].split())[0])[0]) == '-':
            tmp = ((lst_[0].split())[0])
            a1 = only_digit(tmp) * -1
            print(a1)
        else:
            a1 = int(lst_[0])

        a2 = int(lst_[4])
        b1 = only_digit(lst_[2])
        if lst_[1] == '-':
            b1 *= -1
        b2 = only_digit(lst_[6])
        if lst_[5] == '-':
            b2 *= -1
        act1 = lst_[1]
        act2 = lst_[3]
        act3 = lst_[5]







    else:
        print('wtf?')







test = '-34 + 65i - 21 + 67i'.split()
# print(only_digit('34i'))
complex_calc(test)
# calc("6 + 5")