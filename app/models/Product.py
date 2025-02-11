from sqlalchemy import Column, Integer, String, Numeric, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    line = Column(String, nullable=False)


Base.metadata.create_all(engine)
