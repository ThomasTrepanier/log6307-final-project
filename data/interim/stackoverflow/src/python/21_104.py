import re

def split_list(nums, n):
    nums_str = str(nums)
    splits = nums_str.split(f"{n},")

    patc = re.compile(r"\d+")
    group = []
    for part in splits:
        group.append([int(v) for v in patc.findall(part)])

    return group

if __name__ == "__main__":
    l = [1, 2, 3, 4, 3, 6, 7, 3, 8, 9, 10]
    n = 3
    split_l = split_list(l, n)
    assert split_l == [[1, 2], [4], [6, 7], [8, 9, 10]]
