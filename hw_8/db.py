def readit(file):
    with open(file, 'r', encoding='utf-8') as book:
        pwd = book.read()

    pwd = [(int(j[0]), j[1], j[2], int(j[3])) for j in (i.split('\n') for i in (pwd.split('\n\n')))]

    return pwd

def writeit(name, passw):
    count = len(readit('users')) + 1
    with open('users', 'a', encoding='utf-8') as book:
        book.write('\n\n')
        book.write(f'{count}\n')
        book.write(f'{name}\n')
        book.write(f'{passw}\n')
        book.write('2')






