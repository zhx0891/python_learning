import db
def new_user(stat = '2'):
    name = input('придумайте логин: ')
    passw = input('придумайте пароль: ')
    db.writeuser(name, passw, stat)


