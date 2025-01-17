#!/usr/bin/python3
'''
    State class
'''

from models.base_model import BaseModel, Base
from models.city import City
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    else:
        name = ""

    @property
    def cities(self):
        '''
        Get a list of cities based on state.id
        '''
        my_list = []

        cities = models.storage.all(City)
        for city in cities:
            if cities[city].state_id == self.id:
                my_list.append(cities[city])
        return my_list
