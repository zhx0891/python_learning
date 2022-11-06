import db
def view_orders_drivers():
    orders = db.read_order()
    count = 1
    for x in orders:
        print(f'Заказ №: {count} из: {x[1]} в: {x[2]} груз: {x[3]} статус: {x[4]}')
        count += 1
    return count

view_orders_drivers()