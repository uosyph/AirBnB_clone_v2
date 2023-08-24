#!/usr/bin/python3
"""State subclass that inherits from BaseModel"""
import shlex
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """State class to represents new states"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter method for City class"""
        cities = models.storage.all()
        cities_dict = []
        result = []
        for key in cities:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                cities_dict.append(cities[key])
        for key in cities_dict:
            if (key.state_id == self.id):
                result.append(key)
        return result
