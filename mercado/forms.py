from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class Cadastroform(FlaskForm):
    usuario = StringField(label='UserName', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField(label='E-mail', validators=[ Email()])
    senha1 = StringField(label='Senha', validators=[DataRequired(), Length(min=6, max=100)])
    senha2 = StringField(label='Confirme a senha', validators=[DataRequired(), EqualTo('senha1')])
    submit = SubmitField(label='Cadastrar')