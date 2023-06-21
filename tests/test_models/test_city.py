#!/usr/bin/python3
"""TEST """
from tests.test_models.test_base_model import TestBasemodel
from models.city import City
import unittest


class Test_City(TestBasemodel):
    """TEST """

    def __init__(self, *args, **kwargs):
        """TEST """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.name), str)
