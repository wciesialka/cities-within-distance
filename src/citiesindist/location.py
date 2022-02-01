'''Location class container.'''

from __future__ import annotations
from configparser import LegacyInterpolation
from dataclasses import dataclass
from math import atan2, radians, sin, cos, sqrt, pi
from typing import Tuple

RADIUS_EARTH: float = 6371

@dataclass
class Location:

    '''A location on Earth, with latitude and longitude expressed in degrees\
     where negative indicates west/south.'''

    latitude: float
    longitude: float

    def distance(self, other: Location) -> float:
        '''Get distance between two locations in kilometers using Haversine formula.

        :param other: Other location to check
        :type other: Location
        :return: Distance between locations in kilometers.
        :rtype: float
        '''

        lat1 = radians(self.latitude)
        lat2 = radians(other.latitude)
        long1 = radians(self.longitude)
        long2 = radians(other.longitude)

        delta_latitude = lat2 - lat1
        delta_longitude = long2 - long1

        alpha = sin(delta_latitude / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_longitude/2)**2
        charlie = 2 * atan2(sqrt(alpha), sqrt(1-alpha))

        return RADIUS_EARTH * charlie

    def add_distance(self, kilometers: Tuple[float, float]) -> Location:
        '''Create a new location with added distance.

        :param kilometers: A tuple
        :type kilometers: Tuple(float, float)
        :return: A new location
        :rtype: Location
        '''

        dx, dy = kilometers

        latitude = self.latitude + (dy / RADIUS_EARTH) * (180/pi)
        longitude = self.longitude + (dx / RADIUS_EARTH) * (180/pi) / cos(self.latitude * pi/180)

        return Location(latitude, longitude)

    def __str__(self) -> str:
        lat = round(self.latitude, 4)
        lon = round(self.longitude, 4)

        if self.latitude < 0:
            lat = f"{lat}"
        else:
            lat = f"+{lat}"
        if self.longitude < 0:
            lon = f"{lon}"
        else:
            lon = f"+{lon}"
        return f"{lat}{lon}"