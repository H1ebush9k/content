import sqlalchemy.ext.declarative as dec
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class Book(SqlAlchemyBase):
    # создаем бд для книг
    __tablename__ = 'books'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # название книги на родном нам - русском языке
    name_english = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # название книги на английском
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
