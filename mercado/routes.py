
from mercado import app
from mercado.models import Item, User
from flask import render_template, redirect, url_for,flash   
from .forms import Cadastroform
from mercado import db


@app.route('/')
def page_index():
   itens = Item.query.all()
   return render_template('home.html',
                          itens=itens)
   

@app.route('/produtos')
def page_produtos():
    itens = [
        {'id':1,'nome':'teclado','cod_barras':123456,'preco': 100},
        {'id':2,'nome':'mouse','cod_barras':789012,'preco': 50},
        {'id':3,'nome':'monitor','cod_barras':345678,'preco': 1500},
        {'id':4,'nome':'gabinete','cod_barras':901234,'preco': 300},
    ]
    return render_template('produtos.html', itens=itens)

@app.route('/listar_produtos')
def listar_produtos():
    form = Cadastroform()
    itens = Item.query.all()
    return render_template('produtos.html', itens=itens)

@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = Cadastroform() #Instanciando o formulário criado no arquivo forms.py
    if form.validate_on_submit():# Verificando se o formulário foi submetido e se os dados são válidos
        usuario = User(
            username = form.usuario.data,
            email = form.email.data,
            senhacript = form.senha1.data #Criando um novo objeto User com os dados do formulário, nesse caso a senha é configurada usando a propriedade senhacript, que irá criptografar a senha usando bcrypt e armazená-la no banco de dados.
        ) #Criando um novo objeto User com os dados do formulário
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produtos'))
    
    if form.errors != ():
        for err in form.errors.values():
            ##print (f"erro ao cadastar usuario {err}")
            flash(f"erro ao cadastar usuario {err}",category='danger')
    return render_template('cadastro.html', form = form)

'''
@app.route('/about/<usuario>')
def about(usuario):
    return '<h3>About Page</h3><p>This is a simple Flask application. Hello, {}!</p>'.format(usuario)
    '''



''' from mercado import db,app
app.app_context().push()
from mercado.models import User, Item
user1 = User(username='fulano', email='fulano@com.br', senha='123456', valor=100)
db.session.add(user1)
db.session.commit()'''