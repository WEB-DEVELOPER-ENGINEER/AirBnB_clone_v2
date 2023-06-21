#!/usr/bin/python3
'''Tests for DB storage '''
import os
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "Only want to test Database storage")
class testDBStorage(unittest.TestCase):
    '''
    Testing the DB storage class
    '''
    def test_existence_user(self):
        '''
        Testing if User class is being created properly
        '''
        pass
