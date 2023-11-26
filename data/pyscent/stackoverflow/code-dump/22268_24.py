ranges1 = [(1, 50), (49, 70), (75, 85), (84, 88), (87, 92)]
ranges2 = [(1, 50), (40,45), (49, 70)]


def get_overlapping(ranges):
    result = []
    start = 0
    end = ranges[0][1]

    for i, node in enumerate(ranges[1:], 1):
        if end > node[0]:
            if end < node[1]:
                end = node[1]
            continue

        result.append((start, i - 1))
        end = node[1]
        start = i

    else:
        result.append((start, i))
    return result
