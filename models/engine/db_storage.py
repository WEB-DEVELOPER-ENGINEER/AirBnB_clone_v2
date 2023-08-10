#!/usr/bin/python3
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        '''Used to instantiate engine and create attributes'''
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retreive all instances for the specified class"""
        instances = {}
        if cls:
            records = self.__session.query(cls).all()
            for row in records:
                key = cls.__name__ + '.' + row.id
                instances[key] = row
        else:
            clases = [User, Place, State, City, Amenity, Review]
            for clase in clases:
                try:
                    records = self.__session.query(clase).all()
                except Exception:
                    continue
                for record in records:
                    key = "{}.{}".format(type(record).__name__, record.id)
                    instances[key] = record
        return instances

    def new(self, obj):
        '''Add the object to current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''DEletes from the current database'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Creates all database'''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        self.__session.remove()
