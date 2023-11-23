def get_closest_point(self, x, y):
    closest_index = None
    min_distance = float('inf')

    for i, (px, py) in enumerate(self.point_positions):
        distance_squared = (px - x) ** 2 + (py - y) ** 2
        if distance_squared < min_distance:
            min_distance = distance_squared
            closest_index = i

    if min_distance < 25:
        return closest_index, True
    else:
        return closest_index, False
