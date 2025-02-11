from sqlalchemy import Column, Integer, String, Date, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    products = Column(String, nullable=False)


Base.metadata.create_all(engine)
