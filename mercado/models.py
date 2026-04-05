from mercado import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cod_barras = db.Column(db.String(12), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200), nullable=True)

def __repr__(self):
    return f'<Item {self.nome}>'