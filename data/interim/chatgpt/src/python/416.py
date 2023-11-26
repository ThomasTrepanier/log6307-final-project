def DFS_helper(v, time):
    v.status = 'inprogress'
    v.inTime = time
    time += 1
    for w in v.getOutNeighbors():
        if w.status == 'unvisited':
            time = DFS_helper(w, time)
    v.outTime = time
    v.status = 'done'
    print(v, v.inTime, v.outTime)
    return time # return the updated time

def SCC(G):
    time = 0 # initialize time outside the loop
    for v in G.vertices:
        v.status = 'unvisited'
    for v in G.vertices:
        if v.status == 'unvisited':
            time = DFS_helper(v, time) # use the updated time for each DFS call

print(G)
SCCs = SCC(G)
print(SCCs)
