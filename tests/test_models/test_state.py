#!/usr/bin/python3
"""TEST """
from tests.test_models.test_base_model import TestBasemodel
from models.state import State
import unittest


class TestState(test_basemodel):
    """TEST """

    def __init__(self, *args, **kwargs):
        """TEST """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """TEST """
        new = self.value()
        self.assertEqual(type(new.name), str)
