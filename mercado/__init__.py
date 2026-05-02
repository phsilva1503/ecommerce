from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercado.db'
app.config['SECRET_KEY'] = '244466666abcdef1234567890' # Chave secreta para proteger os dados do formulário e sessões
db.init_app(app)
bcrypt.init_app(app)

from mercado import routes


#FORÇA A CRIAÇÃO DO BANCO DE DADOS, RODAR AEPNAS UMA VEZ E CASO SEJA NECESSARIO RECRIAAR O BANCO
"""

with app.app_context():
    db.create_all() """