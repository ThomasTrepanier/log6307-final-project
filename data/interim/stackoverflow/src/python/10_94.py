"""swap mirror node"""
def reverse(arr: List[int]) -> None:
    for i in range(len(arr) // 2):
        arr[i], arr[~i] = arr[~i], arr[i]

"""find median in a sort list"""
def median(arr: List[float]) -> float:
    mid = len(arr) // 2
    return (arr[mid] + arr[~mid]) / 2

"""deal with mirror pairs"""
# verify the number is strobogrammatic, strobogrammatic number looks the same when rotated 180 degrees
def is_strobogrammatic(num: str) -> bool:
    return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num) // 2 + 1))
