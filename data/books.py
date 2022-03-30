import sqlalchemy.ext.declarative as dec
import sqlalchemy
from sqlalchemy import orm

SqlAlchemyBase = dec.declarative_base()


class Book(SqlAlchemyBase):
    __tablename__ = 'book'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    content = orm.relation("Content", back_populates='book')