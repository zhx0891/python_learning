def readit(file):
    with open(file, 'r', encoding='utf-8') as book:
        pwd = book.read()

    pwd = [(int(j[0]), j[1], j[2], int(j[3])) for j in (i.split('\n') for i in (pwd.split('\n\n')))]

    return pwd

def writeuser(name, passw, stat = '2'):
    count = len(readit('users')) + 1
    with open('users', 'a', encoding='utf-8') as book:
        book.write('\n\n')
        book.write(f'{count}\n')
        book.write(f'{name}\n')
        book.write(f'{passw}\n')
        book.write(stat)

def write_order(login):
    client = login
    address = input('Введите адрес отправления:  ')
    destinat = input('Введите адрес назначения:  ')
    cargo = input('Вид груза:  ')
    stat = 'размещён'
    with open('orders', 'a', encoding='utf-8') as order:
        order.write(f'{client}|{address}|{destinat}|{cargo}|{stat}\n\n')

def read_order():
    with open('orders', 'r', encoding='utf-8') as order:
        # ord = (order.read()).split('\n\n')
        return list(map(lambda x: x.split('|'), (order.read()).split('\n\n')))
        # ord = list(filter(lambda x: x[0] == login, (map(lambda x: x.split('|'), (order.read()).split('\n\n')))))



# print(read_order())

# test = readit('users')
# print([list(map(lambda x: print(f'id:{x[0]} login: {x[1]}\n'),(filter(lambda i: i[3] == 1,readit('users')))))])

# print(list(map(lambda y: print(f'из:  {y[1]} в: {y[2]} груз: {y[3]}  статус: {y[4]} \n'),(filter(lambda x: x[0] == 'ЖуковВ', read_order())))))
# print(list((filter(lambda x: x[0] == 'ЖуковВ', read_order()))))

