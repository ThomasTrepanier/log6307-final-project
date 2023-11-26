def get_angles(start_angle=90, increment=-15, return_array_size=12):
    angles = [i for i in range(start_angle + increment, start_angle + (return_array_size*increment) + increment, increment)]
    for index in range(len(angles)):
        while angles[index] < 0:
            angles[index] += 360
    return angles

print(get_angles())
