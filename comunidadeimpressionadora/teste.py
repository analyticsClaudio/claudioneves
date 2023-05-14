from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario


with app.app_context():
    database.create_all()

# with app.app_context():
#      database.drop_all()

# with app.app_context():
#     Usuario.query.all()
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.username)
#     print(meus_usuarios.email)
#     print(meus_usuarios.senha)
