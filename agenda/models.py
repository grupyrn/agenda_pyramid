from sqlalchemy import (
    Column, Index, Integer,
    ForeignKey, Unicode, UnicodeText,
    Time, Date
)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
)
from zope.sqlalchemy import ZopeTransactionExtension
from pyramid.threadlocal import get_current_request

import sqlalchemy as sa


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class BaseModify(object):
    """
    Todas as classes que heram de BaseModify, sao criadas por padrao um ID,
    e nao se faz necessario colocar em todas, __tablename__, que o sqlalchemy
    exige para nomear as tabelas.

    Fique a vontade para alterar essa classe ao seu gosto
    """
    @declared_attr
    def pk(cls):
        return Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    def all(cls):
        return DBSession.query(cls).all()

    @classmethod
    def by_id(cls, pk):
        return DBSession.query(cls).filter(cls.pk == pk).first()

    @classmethod
    def filter_by(cls, **kw):
        return DBSession.query(cls).filter_by(**kw)

Base = declarative_base(cls=BaseModify)


class Agenda(Base):
    nome = Column(Unicode(50))


class ItemAgenda(Base):
    """
    item = ItemAgenda.by_id(1)
    item.agenda -> Acessa todos os atributos de Agenda()
    """
    agenda_id = Column(Integer, ForeignKey(Agenda.pk), nullable=False)
    titulo = Column(Unicode(100), nullable=False)
    descricao = Column(UnicodeText)
    data = Column(Date)
    hora = Column(Time)
    agenda = relationship(Agenda)

Index('my_index_agenda', Agenda.nome, unique=True, mysql_length=255)
Index('my_index_item_agenda', ItemAgenda.titulo, unique=True, mysql_length=255)
