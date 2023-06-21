#!/usr/bin/python3
"""TEST """
from tests.test_models.test_base_model import TestBasemodel
from models.user import User
import os
import unittest


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "test FileStorage")
class TestUser(TestBasemodel):
    """TEST """

    def __init__(self, *args, **kwargs):
        """TEST """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.password), str)
