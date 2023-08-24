#!/usr/bin/python3
"""City subclass that inherits from BaseModel"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """City class to represent new cities"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)
    places = relationship("Place",
                          cascade='all, delete, delete-orphan',
                          backref="cities")
