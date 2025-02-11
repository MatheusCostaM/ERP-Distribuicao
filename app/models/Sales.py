from sqlalchemy import Column, Integer, Date, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)


Base.metadata.create_all(engine)
