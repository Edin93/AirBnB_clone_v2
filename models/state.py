#!/usr/bin/python3
"""
This is the state class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            cascade="all,delete",
            backref="state"
        )
    else:
        name = ''

        @property
        def cities(self):
            """Returns the list of Cities with the correspondant state_id
        """
        cities = models.storage.all(City)
        cities_list = []
        for k, v in cities.items():
            if v.state_id == self.id:
                cities_list.append(v)
                return(cities_list)
