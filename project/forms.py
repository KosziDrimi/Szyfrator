from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField, TimeField, EmailField



class EnquiryForm(FlaskForm):

    word = StringField('* Podaj słowo / krótki tekst do zaszyfrowania:', validators=[DataRequired()])
    method = SelectField('* Wybierz metodę szyfrowania:', validators=[DataRequired()], 
            choices=[('gaderypoluki', 'Gaderypoluki'), ('politykarenu', 'Politykarenu'), 
                     ('both', 'Obie - Gaderypoluki i Politykarenu')])
    submit = SubmitField('Pokaż rezultat')


class EmailForm(FlaskForm):
    email = EmailField('* Podaj adres e-mail:', validators=[DataRequired(), Email()])
    submit = SubmitField('Wyślij e-mail z wynikiem szyfrowania')