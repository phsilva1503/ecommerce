from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField


class Cadastroform(FlaskForm):
    usuario = StringField('Usuário')
    email = StringField('E-mail')
    senha1 = StringField('Senha')
    senha2 = StringField('Confirme a senha')
    submit = SubmitField('Cadastrar')