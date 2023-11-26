def shortest_equivalent_binarian(A): 
   s = set() 
   for a in A: 
       while a in s: # carry propagation
           s.remove(a) 
           a += 1 
       s.add(a) 
   return sorted(s, reverse=True)
# reverse is not necessary for correctness, but gives the same B as in your example
