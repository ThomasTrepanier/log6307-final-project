def sort_and_extract_non_zero_items(items: list) -> Iterable:
  return sorted([n for n in l if n != 0])

def replace_non_zero_items(original: list, non_zeroes: list) -> Iterable:
  return [non_zeroes.pop(0) if n != 0 else 0 for n in original]

non_zero_list = sort_and_extract_non_zero_items(items)

items = replace_non_zero_items(items, non_zero_list)
