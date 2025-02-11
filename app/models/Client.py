from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    nickname = Column(String)
    cpf = Column(Integer, nullable=True)
    cnpj = Column(Integer, nullable=True)
    payment_time = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
