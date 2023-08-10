#!/usr/bin/python3
'''
    Class City.
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='city')
    else:
        state_id = ""
        name = ""
