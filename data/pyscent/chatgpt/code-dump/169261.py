def get_closest_point(self, x, y):
    def distance_squared(point):
        px, py = point
        return (px - x) ** 2 + (py - y) ** 2

    if not self.point_positions:
        return None, False

    distances = [distance_squared(point) for point in self.point_positions]
    min_distance = min(distances)
    closest_index = distances.index(min_distance)

    if min_distance < 25:
        return closest_index, True
    else:
        return None, False
