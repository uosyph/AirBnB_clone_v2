#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if (environ.get("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """ Getter method for City class """
            cities_dict = []
            for key in storage.all(City):
                if self.id in storage.all(City)[key].state_id:
                    cities_dict.append(storage.all(City)[key])
            return cities_dict
