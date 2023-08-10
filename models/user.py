#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User  attributes"""
    __tablename__ = 'users'
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade='delete')
    reviews = relationship('Review', backref='user', cascade='delete')
