import db
def new_user():
    name = input('придумайте логин: ')
    passw = input('придумайте пароль: ')
    db.writeit(name, passw)

