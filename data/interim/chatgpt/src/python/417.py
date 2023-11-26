def DFS_helper(v, time, component):
    v.status = 'inprogress'
    component.append(v) # add the vertex to the current component
    v.inTime = time
    time += 1
    for w in v.getOutNeighbors():
        if w.status == 'unvisited':
            time = DFS_helper(w, time, component)
    v.status = 'done'
    v.outTime = time
    time += 1
    return time

def SCC(G):
    time = 1 # initialize time outside the loop
    for v in G.vertices:
        v.status = 'unvisited'
    for v in G.vertices:
        if v.status == 'unvisited':
            DFS_helper(v, time, [])
    
    for v in G.vertices:
        for w in v.getOutNeighbors():
            G.reverseEdge(v, w)
    
    # Repeat the DFS loop, but this time on the reversed graph
    time = 1
    SCCs = [] # list to store all SCCs
    for v in G.vertices:
        v.status = 'unvisited'
    stack = sorted(G.vertices, key=lambda x: x.outTime, reverse=True)
    for v in stack:
        if v.status == 'unvisited':
            component = [] # list to store the current SCC
            time = DFS_helper(v, time, component)
            SCCs.append(component)
    
    # print the SCCs, each on a new line
    for scc in SCCs:
        print([str(v) for v in scc])
    
    return SCCs

SCCs = SCC(G)
