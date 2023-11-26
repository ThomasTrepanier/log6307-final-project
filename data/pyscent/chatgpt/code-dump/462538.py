def prim(G, s):
    MST = [s]
    Q = queue.PriorityQueue()
    # add all edges from s to Q
    for v, wt in s.getOutNeighborsWithWeights():
        Q.put((wt, s, v))  # weight first
    print(Q.queue)
    while not Q.empty():
        # extract min edge from Q
        wt, u, v = Q.get()
        if v not in MST:
            MST.append(v)
            print("Adding edge", u, v, "to MST")
            for w, wt in v.getOutNeighborsWithWeights():
                Q.put((wt, v, w))  # weight first
