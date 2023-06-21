#!/usr/bin/python3
"""TEST """
from tests.test_models.test_base_model import TestBasemodel
from models.review import Review
import os
import unittest


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 "test only for FileStorage")
class TestReview(TestBasemodel):
    """TEST """

    def __init__(self, *args, **kwargs):
        """TEST """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.text), str)
