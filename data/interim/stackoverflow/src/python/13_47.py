B = [0.6, 1.7, 3, 4.5]
A = [0.6, 0.9, 1.2, 1.5, 2, 2.5, 3, 4, 4.5]

def first_greater_elem(lst, elem):
    for item in lst:
       if item >= elem:
         return item
