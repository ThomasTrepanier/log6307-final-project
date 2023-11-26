import itertools

def get_closest_point(self, x, y):
    def distance_squared(point):
        px, py = point
        return (px - x) ** 2 + (py - y) ** 2

    if not self.point_positions:
        return None, False

    closest_point = min(self.point_positions, key=distance_squared)
    min_distance = distance_squared(closest_point)

    if min_distance < 25:
        closest_index = self.point_positions.index(closest_point)
        return closest_index, True
    else:
        return None, False
