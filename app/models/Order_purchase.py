from sqlalchemy import Column, Integer, String, Date, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/erp.db')

Base = declarative_base


class OrderPurchase(Base):
    __tablename__ = 'order_purchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchases = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)


Base.metadata.create_all(engine)
