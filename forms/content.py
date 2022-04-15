from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ContentForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание", validators=[DataRequired()])
    short_content = StringField('Краткое содержание (не более 120 симфолов)', validators=[DataRequired()])
    book = StringField('Название книги на английском', validators=[DataRequired()])
    submit = SubmitField('Добавить содержание')