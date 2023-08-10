#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import relationship_table

class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=relationship_table)
    else:
        name = ""
