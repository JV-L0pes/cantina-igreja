from sqlalchemy import Column, Integer, String, Float

class ProductModel:
    __tablename__ = 'products'

    id = Column(Integer)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
