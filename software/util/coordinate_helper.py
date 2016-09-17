import random
import math
from haversine import haversine


def random_coordinate():
    # TODO remove this method once we have a way to actually get coordiantes from the base station
    lat = -41.2880647 + (random.random() / 100)
    long = 174.7617035 + (random.random() / 100)

    return lat, long


def distance_between_coordinates(current_coordinate, target_coordinate):
    distance_in_km = haversine(current_coordinate, target_coordinate)
    distance_in_metres = math.ceil(distance_in_km * 1000)
    return distance_in_metres
