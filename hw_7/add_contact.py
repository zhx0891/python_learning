
def doit():
    print('Добавляю контакт\n')
    name = input(' Имя Фамилия: \n')
    phone = input(' Номер телефона: \n')
    comment = input(' Комментарий: \n')
    with open('phonebook', 'a', encoding='utf-8') as book:
        book.write(f'{name} \n')
        book.write(f'{phone} \n')
        book.write(f'{comment} \n')
        book.write(f'\n')


print('Контакт добавлен.')




