from itertools import combinations

teams = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
combo = list(combinations(teams, 2))

sets = []

def is_combo_value_in_set(c, s):
    for val in c:
        for val_s in s:
            for v in val_s:
                if val == v:
                    return True
    return False

for c in combo:
    should_add_set = True
    for current_set in sets:
        if is_combo_value_in_set(c, current_set) is False:
            should_add_set = False
            current_set.add(c)
            break
    if should_add_set:
        sets.append(set())
        sets[-1].add(c)

for v in sets:
    print(sorted(v))
