import math
from haversine import haversine


def distance_between_coordinates(current_coordinate, target_coordinate):
    """
        Calculates the Haversine distance between two lat-long coordinates

    :return:
        Distance in metres
    """
    distance_in_km = haversine(current_coordinate, target_coordinate)
    distance_in_metres = math.ceil(distance_in_km * 1000)
    return distance_in_metres


def bearing_between_coordinates(current_coordinate, target_coordinate):
    """
        The formulae used is the following:
            θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))

    :returns:
        The Bearing in degrees

    :return type:
        float
    """
    current_lat = math.radians(current_coordinate[0])
    target_lat = math.radians(target_coordinate[0])

    diff_long = math.radians(target_coordinate[1] - current_coordinate[1])

    x = math.sin(diff_long) * math.cos(target_lat)
    y = math.cos(current_lat) * math.sin(target_lat) - \
        (math.sin(current_lat) * math.cos(target_lat) * math.cos(diff_long))

    bearing = math.atan2(x, y)

    # math.atan2 returns values from -180..180 degrees. Therefore we normalise to a compass bearing
    bearing = math.degrees(bearing)
    compass_bearing = (bearing + 360) % 360

    return compass_bearing
