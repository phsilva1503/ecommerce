from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from mercado.models import User


class Cadastroform(FlaskForm):

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username já existe. Por favor, escolha outro.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail já cadastrado. Por favor, escolha outro.')
    def validade_senha1(self, senha1):
        senha  = User.query.filter_by (senha=senha1.data).first()
        if senha:
            raise ValidationError('Senha já existe. Por favor, escolha outra.')
        

    usuario = StringField(label='UserName', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField(label='E-mail', validators=[ Email()])
    senha1 = StringField(label='Senha', validators=[DataRequired(), Length(min=6, max=100)])
    senha2 = StringField(label='Confirme a senha', validators=[DataRequired(), EqualTo('senha1')])
    submit = SubmitField(label='Cadastrar')