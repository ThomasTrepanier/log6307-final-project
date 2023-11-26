def contains(seq, sub):
    sub_length = len(sub)
    sub_first = sub[0]
    return any(sub == seq[index:index+sub_length]
               for index, element in enumerate(seq)
               if element == sub_first)
