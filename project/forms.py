from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired



class EnquiryForm(FlaskForm):

    word = StringField('* Podaj słowo / krótki tekst do zaszyfrowania:', validators=[DataRequired()])
    method = SelectField('* Wybierz metodę szyfrowania:', validators=[DataRequired()], 
            choices=[('gaderypoluki', 'Gaderypoluki'), ('politykarenu', 'Politykarenu'), 
                     ('both', 'Obie - Gaderypoluki i Politykarenu')])
    submit = SubmitField('Pokaż rezultat')


