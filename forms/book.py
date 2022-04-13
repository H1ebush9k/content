from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    name = StringField('Название книги', validators=[DataRequired()])
    name_english = StringField("Название книги на английском")
    author = StringField('Автор')
    year = StringField('Год создания книги')
    submit = SubmitField('Применить')
