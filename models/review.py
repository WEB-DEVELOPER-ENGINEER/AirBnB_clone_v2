#!/usr/bin/python3
'''
    Review class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "reviews"
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
