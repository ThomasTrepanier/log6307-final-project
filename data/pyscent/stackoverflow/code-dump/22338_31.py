def overlaps(r1, r2):
    assert r1[0] <= r2[0], "Assume ranges sorted by first coordinate"
    return (r2[0] <= r1[1] <= r2[1]) or (r1[0] <= r2[0] <= r1[1])

ranges = [(1, 50), (45, 47), (49, 70), (75, 85), (84, 88), (87, 92)]


def fuse_ranges(ranges):
    output_ranges = []
    curr_r = list(ranges[0])
    curr_overlap = False  # Is the current range already overlapping?

    # Assuming it is sorted by starting coordinate.
    for r in ranges[1:]:
        if overlaps(curr_r, r):
            curr_overlap = True
            curr_r[1] = max(curr_r[1], r[1])  # Extend the end of the current range.
        else:
            if curr_overlap:
                output_ranges.append(curr_r)
                curr_overlap = False
            curr_r = list(r)
    if curr_overlap:
        output_ranges.append(curr_r)

    return output_ranges


if __name__ == '__main__':
    print(fuse_ranges(sorted(ranges, key=lambda r: r[0])))
