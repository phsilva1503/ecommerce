from mercado import db
from mercado import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref='dono_user', lazy=True)

    @property #A propriedade senhacript é definida para retornar a senha criptografada do usuário. Ela é decorada com @property, o que significa que pode ser acessada como um atributo, sem a necessidade de chamar um método. Quando você acessar user.senhacript, ele retornará a senha criptografada armazenada no banco de dados.
    def senhacript(self): #A propriedade senhacript é definida para retornar a senha criptografada do usuário. Ela é decorada com @property, o que significa que pode ser acessada como um atributo, sem a necessidade de chamar um método. Quando você acessar user.senhacript, ele retornará a senha criptografada armazenada no banco de dados.
        return self.senhacript  #A propriedade senhacript é definida para retornar a senha criptografada do usuário. Ela é decorada com @property, o que significa que pode ser acessada como um atributo, sem a necessidade de chamar um método. Quando você acessar user.senhacript, ele retornará a senha criptografada armazenada no banco de dados.
    
    @senhacript.setter #O método setter é definido para permitir que a senha seja configurada usando a propriedade senhacript. Ele é decorado com @senhacript.setter, o que significa que pode ser usado para atribuir um valor à propriedade senhacript. Quando você fizer user.senhacript = 'minhasenha', o método setter será chamado, e ele irá criptografar a senha usando bcrypt e armazená-la no banco de dados.
    def senhacript(self, senha_texto): #O método setter é definido para permitir que a senha seja configurada usando a propriedade senhacript. Ele é decorado com @senhacript.setter, o que significa que pode ser usado para atribuir um valor à propriedade senhacript. Quando você fizer user.senhacript = 'minhasenha', o método setter será chamado, e ele irá criptografar a senha usando bcrypt e armazená-la no banco de dados.
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8') #O método setter é definido para permitir que a senha seja configurada usando a propriedade senhacript. Ele é decorado com @senhacript.setter, o que significa que pode ser usado para atribuir um valor à propriedade senhacript. Quando você fizer user.senhacript = 'minhasenha', o método setter será chamado, e ele irá criptografar a senha usando bcrypt e armazená-la no banco de dados.



    def __repr__(self):
        return f'<User {self.username}>'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cod_barras = db.Column(db.String(12), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Item {self.nome}>'