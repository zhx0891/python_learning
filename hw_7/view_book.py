import proxy as m

def doit():
    with open('phonebook', 'r', encoding='utf-8') as book:
        print(book.read())

    m.itswork()