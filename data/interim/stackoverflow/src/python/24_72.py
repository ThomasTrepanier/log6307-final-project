def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  buf = list2[:] # or list2.copy()
  buf.extend(reversed(list1))
  return buf


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]                     
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
