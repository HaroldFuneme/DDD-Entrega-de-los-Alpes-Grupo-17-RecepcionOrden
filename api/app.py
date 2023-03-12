import uuid
from api import create_app
from recepcion_orden import recepcion_orden_bp
from infraestructura.dto import db, OrdenDTO, ItemDTO



# app = create_app('default')
# app.register_blueprint(recepcion_orden_bp)
# app_context = app.app_context()
# app_context.push()


# db.init_app(app)
# db.create_all()
# with app.app_context():
#     item1 = ItemDTO(item='pantalon1')
#     item2 = ItemDTO(item='pantalon2')
#     item3 = ItemDTO(item='pantalon3')

#     ord = OrdenDTO(user='usuario1', user_address='call 35 65 43', items=[item1,item2,item3])

#     db.session.add(ord)
#     db.session.add(item1)
#     db.session.add(item2)
#     db.session.add(item3)
#     db.session.commit()
#     print(OrdenDTO.query.all())
#     print(ItemDTO.query.all())
#     print("HHFMTT")

