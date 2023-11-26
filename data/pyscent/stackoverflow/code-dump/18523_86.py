li1 = [6, 0, 4, 8, 7, 6]
li2 = [1, 4, 1, 2, 4, 3, 5, 4, 0]

def inc_seq(li1):
  lix = []
  li_t = [] 
  for i in range(len(li1)):
    #print (i)
    if i < (len(li1) - 1) and li1[i] >= li1[i + 1]:
      li_t.append(li1[i])
      lix.append(li_t)
      li_t = []
    else:
      li_t.append(li1[i])


  print (lix)

inc_seq(li1)
inc_seq(li2)
