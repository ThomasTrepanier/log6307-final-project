def prim(G, s):
    MST = set([s])  # Use a set for faster look-up
    Q = queue.PriorityQueue()
    # add all edges from s to Q
    for v, wt in s.getOutNeighborsWithWeights():
        Q.put((wt, s, v))  # weight first
    while not Q.empty():
        # extract min edge from Q
        wt, u, v = Q.get()
        if v not in MST:
            MST.add(v)  # Use add method for set
            print("Adding edge", u, v, "to MST")
            for w, wt in v.getOutNeighborsWithWeights():
                Q.put((wt, v, w))  # weight first
