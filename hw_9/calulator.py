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
            
        # print('ok')

    else:
        print('wtf?')







test = '-34 + 65i - 21 + 67i'.split()
print(test)
complex_calc(test)
# calc("6 + 5")