'''Main module.'''

from math import sin, radians, cos
import requests
from citiesindist.location import Location

def request(location: Location):

    # http://wft-geo-db.p.rapidapi.com/v1/geo/locations/{locationId}/nearbyCities?limit=5&offset=0&radius=100

    endpoint = f"https://wft-geo-db.p.rapidapi.com/v1/geo/locations/{location}/nearbyCities?limit=5&offset=0&radius=100"
    r = requests.get(endpoint)

    print(r)

def main():
    '''Main function.
    '''
    # The number of kilometers per degree of latitude
    #  is approximately the same at all locations, approx 111 km
    step = 1

    lat = float(input("Your latitude: "))
    long = float(input("Your longitude: "))
    loc = Location(lat, long)

    locations = []

    dist = float(input("Distance: "))
    
    for degree in range(0, 360, step):
        theta = radians(degree)
        dx = dist * sin(theta)
        dy = dist * cos(theta)

        new_loc = loc.add_distance((dx, dy))
        locations.append(new_loc)

    request(locations[0])


if __name__ == "__main__":
    main()
