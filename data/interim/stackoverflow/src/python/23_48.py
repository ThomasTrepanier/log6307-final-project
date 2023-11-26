from typing import Dict, List, Any, Set

d = {"level":[1,2,3], "conf":[-1,1,2], "text":["-1", "hel", "llo"]}

# First, we create a set that stores the indices which should be kept.
# I chose a set instead of a list because it has a O(1) lookup time.
# We only want to keep the items on indices where the value in d["conf"] is greater than 0
filtered_indexes = {i for i, value in enumerate(d.get('conf', [])) if value > 0}

def filter_dictionary(d: Dict[str, List[Any]], filtered_indexes: Set[int]) -> Dict[str, List[Any]]:
    filtered_dictionary = d.copy()  # We'll return a modified copy of the original dictionary
    for key, list_values in d.items():
        # In the next line the actual filtering for each key/value pair takes place. 
        # The original lists get overwritten with the filtered lists.
        filtered_dictionary[key] = [value for i, value in enumerate(list_values) if i in filtered_indexes]
    return filtered_dictionary

print(filter_dictionary(d, filtered_indexes))
