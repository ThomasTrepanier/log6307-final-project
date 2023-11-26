import math
from math import sin, cos, sqrt, atan2, radians

def get_distance(in_lat1, in_lon1, in_lat2, in_lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(in_lat1)
    lon1 = radians(in_lon1)
    lat2 = radians(in_lat2)
    lon2 = radians(in_lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
