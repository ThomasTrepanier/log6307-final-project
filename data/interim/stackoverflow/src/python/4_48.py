# use an alias so I don't have to remember to avoid using "approx" as a variable name
from pytest import approx as pytest_approx


def is_primitive(x):
    return x is None or type(x) in (int, float, str, bool)


def approx_equal(A, B, absolute=1e-6, relative=1e-6, enforce_same_type=False):
    if enforce_same_type and type(A) != type(B) and not is_primitive(A):
        # I use `not is_primitive(A)` to enforce the same type only for data structures
        return False

    try:
        is_approx_equal = (A == pytest_approx(B, rel=relative, abs=absolute))
    except TypeError:
        is_approx_equal = False

    if is_approx_equal:
        # pytest_approx() can only compare primitives and non-nested data structures correctly
        # If the data structures are nested, then approx_equal() will try one of the other branches
        return True
    elif is_primitive(A) or is_primitive(B):
        return False
    elif isinstance(A, set) or isinstance(B, set):
        # if any of the data structures is a set, convert both of them to a sorted list, but return False if the length has changed
        len_A, len_B = len(A), len(B)
        A, B = sorted(A), sorted(B)
        if len_A != len(A) or len_B != len(B):
            return False

        for i in range(len(A)):
            if not approx_equal(A[i], B[i], absolute, relative):
                return False

        return True
    elif isinstance(A, dict) and isinstance(B, dict):
        for k in A.keys():
            if not approx_equal(A[k], B[k], absolute, relative):
                return False

        return True
    elif (isinstance(A, list) or isinstance(A, tuple)) and (isinstance(B, list) or isinstance(B, tuple)):
        for i in range(len(A)):
            if not approx_equal(A[i], B[i], absolute, relative):
                return False

        return True
    else:
        return False


print(approx_equal([1], {1.000001}, enforce_same_type=True)) # False
print(approx_equal([1], {1.000001}, enforce_same_type=False)) # True

print(approx_equal([123.001, (1,2)], [123, (1,2)])) # False
print(approx_equal([123.000001, (1,2)], [123, (1,2)])) # True

print(approx_equal({'a': {'b': 1}, 'c': 3.141592}, {'a': {'b': 1.0000005}, 'c': 3.1415})) # False
print(approx_equal({'a': {'b': 1}, 'c': 3.141592}, {'a': {'b': 1.0000005}, 'c': 3.141592})) # True
