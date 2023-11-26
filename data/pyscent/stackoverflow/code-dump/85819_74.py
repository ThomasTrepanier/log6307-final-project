def mirror_numbers(start,stop):
  if start<stop:
    val=range(start,stop)
    return [j if i < len(val) else -j for i,j in enumerate([x for x in val]*2) ]

mirror_numbers(6,10)
