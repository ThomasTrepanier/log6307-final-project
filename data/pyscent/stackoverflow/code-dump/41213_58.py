def round_the_list(list, bound_1, bound_2):
  mid = (bound_1+bound_2)/2
  for i in range(len(list)):
        if list[i] > mid:         # or >= depending on your rounding decision
            list[i] = bound_2
        else:
            list[i] = bound_1
