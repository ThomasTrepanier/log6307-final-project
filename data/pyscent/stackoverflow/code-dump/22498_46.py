def find_cycles(indices):
    """Given a list of indices return a list of cycles."""

    visited = set()
    cycles = []

    for start_ind in indices:

        if start_ind in visited:
            continue

        path = [start_ind]
        next_ind = indices[start_ind]

        while start_ind != next_ind:
            path.append(next_ind)
            next_ind = indices[next_ind]
        else:
            cycles.append(path)
            visited |= set(path)
    return cycles

find_cycles([12, 0, 8, 10, 9, 6, 5, 4, 13, 7, 17,14, 2,18, 16, 1, 11, 19, 3, 15])
# [[12, 2, 8, 13, 18, 3, 10, 17, 19, 15, 1, 0], [9, 7, 4], [6, 5], [14, 16, 11]]
