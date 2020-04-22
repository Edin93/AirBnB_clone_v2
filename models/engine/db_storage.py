#!/usr/bin/python3
"""
The Database Storage Engine that will connect our python classes
with the MySQL database.
"""
from models.base_model import Base
from sqlalchemy import create_engine, MetaData, Table
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """The database storage engine of our application.
    """

    __engine = None
    __session = None
    my_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """Constructor of the DBStorage class.
        """
        url = "mysql+mysqldb://{}:{}@{}/{}".format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')
        )
        self.__engine = create_engine(url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects depending
        on the class name argument (cls).
        """
        d = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                k = str(cls) + '.' + obj.id
                d[k] = obj
            return(d)
        else:
            for cl in self.my_classes:
                for obj in self.__session.query(eval(cl)):
                    k = str(cl) + '.' + obj.id
                    d[k] = obj
            return(d)

    def new(self, obj):
        """Adds the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """Commit all the changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None.
        """
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current databse
        session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Call remove() method on the private session attribute.
        """
        return self.__session.remove()
