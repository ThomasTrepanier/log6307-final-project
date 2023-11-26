from typing import Any, Tuple, Generator, FrozenSet

def search_in_dict(d: Any, keys: FrozenSet[str]) -> Generator[Tuple[str, Any], None, None]:
    """
    Generate pairs key-value for found keys
    """
    if not isinstance(d, dict):
        return
    for key, value in d.items():
        if key in keys:
            if isinstance(value, dict):
                # Special case: return the first key from nested dict as value
                yield key, tuple(value.keys())[0]
            else:
                yield key, value
        # continue to search deeper
        yield from search_in_dict(value, keys)
