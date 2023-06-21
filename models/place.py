#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel):
    """This is the class for Place
    """
    @property
    def reviews(self):
        """ Returns list of reviews.id """
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            review = key.replace('.', ' ')
            review = shlex.split(review)
            if (review[0] == 'Review'):
                lista.append(var[key])
        for elem in lista:
            if (elem.place_id == self.id):
                result.append(elem)
        return (result)

    @property
    def amenities(self):
        """ Returns list of amenity ids """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """ Appends amenity ids to the attribute """
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
