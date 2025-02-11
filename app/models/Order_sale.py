from sqlalchemy import Column, Integer, String, Date, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class OrderSale(Base):
    __tablename__ = 'order_sale'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sales = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)


Base.metadata.create_all(engine)
