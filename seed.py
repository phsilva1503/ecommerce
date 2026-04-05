from mercado import app, db
from mercado.models import User, Item

# Ativa o contexto da aplicação
app.app_context().push()

# Criar usuário
user1 = User(username='beltrano', email='beltrano@com.br', senha='123', valor=100)
db.session.add(user1)
db.session.commit()

# Criar item
item1 = Item(nome='Teclado', cod_barras='123456789012', preco=150.0, descricao='Teclado mecânico', dono=user1.id)
db.session.add(item1)
db.session.commit()

print("Usuário e item criados com sucesso!")