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

def read_order(login):
    with open('orders', 'r', encoding='utf-8') as order:
        return list(filter(lambda x: x[0] == login, (map(lambda x: x.split('|'), (order.read()).split('\n\n')))))


print(read_order('ЖуковВ'))

# test = readit('users')
# print([list(map(lambda x: print(f'id:{x[0]} login: {x[1]}\n'),(filter(lambda i: i[3] == 1,readit('users')))))])




