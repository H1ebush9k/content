from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    name = StringField("Название книги", validators=[DataRequired()])
    name_english = StringField("Название книги на английском", validators=[DataRequired()])
    author = StringField("Имя автора", validators=[DataRequired()])
    year = IntegerField("Год выхода", validators=[DataRequired()])
    submit = SubmitField("Добавить книгу", validators=[DataRequired()])