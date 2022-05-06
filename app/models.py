from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base

class Item(Base):
	__tablename__ = "items"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(80), nullable=False, unique=True,index=True)
	price = Column(Float(precision=2), nullable=False)
	description = Column(String(200))
	store_id = Column(Integer,ForeignKey('stores.id'),nullable=False)