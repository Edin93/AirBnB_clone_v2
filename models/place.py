#!/usr/bin/python3
"""This is the place class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship(
        "Review",
        cascade="all,delete",
        backref='place'
    )

    metadata = Base.metadata

    place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
        ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
        )
    )

    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        viewonly=False
    )

    @property
    def amenities(self):
        """
        """
        amenities = models.storage.all(Amenity)
        d = []
        for k, v in amenities.items():
            if v.id in self.amenity_ids:
                d[k] = v
        return(d)

    @amenities.setter
    def amenities(self, obj):
        """
        """
        if Amenity == type(obj):
            self.amenity_ids.append(obj.id)

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id equals to
        the current Place.id.
        """
        reviews = models.storage.all(Review)
        d = {}
        for k, v in reviews.items():
            if v.place_id == self.id:
                d[k] = v
        return(d)
