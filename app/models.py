from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base

class Item(Base):
	__tablename__ = "items"

	id = Column(Integer, primary_key=True, index=True)