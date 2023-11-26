def get_date_ranges(pto_list: list) -> list:
    pto_dates = [datetime.datetime.strptime(i, '%Y-%m-%d').toordinal() for i in pto_list]
    nums = sorted(set(pto_dates))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s + 1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    ordinal_ranges = list(zip(edges, edges))
    date_bounds = []
    for start, end in ordinal_ranges:
        date_bounds.append((
            datetime.datetime.fromordinal(start).strftime('%Y-%m-%d'),
            datetime.datetime.fromordinal(end).strftime('%Y-%m-%d')
        ))
    return date_bounds
