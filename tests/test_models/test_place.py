#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place
import os
import unittest

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class TestPlace(TestBasemodel):
    """TEST """

    def __init__(self, *args, **kwargs):
        """TEST """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
