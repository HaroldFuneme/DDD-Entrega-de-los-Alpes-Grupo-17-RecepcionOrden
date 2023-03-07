import uuid
from api import create_app
from infraestructura.dto import db, Orden, Item

app = create_app('default')
app_context = app.app_context()
app_context.push()

    

db.init_app(app)
db.create_all()
with app.app_context():
    item1 = Item(item='pantalon1')
    item2 = Item(item='pantalon2')
    item3 = Item(item='pantalon3')

    ord = Orden(user='usuario1', user_address='call 35 65 43', items=[item1,item2,item3])

    db.session.add(ord)
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.commit()
    print(Orden.query.all())
    print(Item.query.all())
    print("HHFMTT")

