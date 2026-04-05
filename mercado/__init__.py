from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercado.db'
db.init_app(app)

from mercado import routes


#FORÇA A CRIAÇÃO DO BANCO DE DADOS, RODAR AEPNAS UMA VEZ E CASO SEJA NECESSARIO RECRIAAR O BANCO
'''with app.app_context():
    db.create_all()'''