#!/usr/bin/python3
"""TEST """
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity
import os
import unittest


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class Test_Amenity(TestBasemodel):
    """TEST """

    def __init__(self, *args, **kwargs):
        """TEST """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.name), str)
