import sqlalchemy.ext.declarative as dec
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class Book(SqlAlchemyBase):
    __tablename__ = 'books'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name_english = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    content = orm.relation("Content", back_populates='book')