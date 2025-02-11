from sqlalchemy import Column, Integer, Numeric, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    value = Column(Numeric(10, 2), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)


Base.metadata.create_all(engine)
