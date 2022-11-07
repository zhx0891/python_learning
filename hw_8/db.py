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
    count = len(read_order()) + 1
    with open('orders', 'a', encoding='utf-8') as order:
        order.write(f'{count}|{client}|{address}|{destinat}|{cargo}|{stat}\n')

def read_order():
    with open('orders', 'r', encoding='utf-8') as order:
        # return (order.read()).split('\n\n')
        e = list(map(lambda x: x.split('|'), (order.read()).split('\n')))
        e.pop()
        return e
        # return list(filter(lambda x: x[0] == login, (map(lambda x: x.split('|'), (order.read()).split('\n\n')))))

def view_orders_drivers():
    orders = read_order()
    count = 1
    for x in orders:
        print(f'Заказ №: {x[0]} из: {x[2]} в: {x[3]} груз: {x[4]} статус: {x[5]}')
        count += 1
    return count

def add_route(login, id):

    order = list(filter(lambda x: x[0] == id, read_order()))
    order = order[0]
    rt = f'Заказ №: {order[0]} из: {order[2]} в: {order[3]} груз: {order[4]} статус: исполняется водителем {login}'

    change_order(order[0])
    with open('routes', 'a', encoding='utf-8') as route:
        route.write(rt)



def change_order(n):
    with open('orders', 'r', encoding='utf-8') as order:
        ord = order.readlines()

    with open('orders', 'w', encoding='utf-8') as order:
        for ind, item in enumerate(ord):
            e = item.split('|')
            if e[0] == n:
                order.write(f'{e[0]}|{e[1]}|{e[2]}|{e[3]}|{e[4]}|в работе\n')
            else:
                order.write(f'{e[0]}|{e[1]}|{e[2]}|{e[3]}|{e[4]}|{e[5]}')









# change_order('10')
# add_route('test', '1')
# print(read_order())

# test = readit('users')
# print([list(map(lambda x: print(f'id:{x[0]} login: {x[1]}\n'),(filter(lambda i: i[3] == 1,readit('users')))))])

# print(list(map(lambda y: print(f'из:  {y[1]} в: {y[2]} груз: {y[3]}  статус: {y[4]} \n'),(filter(lambda x: x[0] == 'ЖуковВ', read_order())))))
# print(list((filter(lambda x: x[0] == 'ЖуковВ', read_order()))))

# write_order('test')
# print(read_order())