def BidirectionalSearch(s, t, G):
    for v in G.vertices:
        v.status = 'unvisited'

    # Dictionaries to store paths
    path_from_s = {s: [s]}
    path_from_t = {t: [t]}

    Ls1 = [s]
    Ls2 = [t]
    s.status = 'visitedByS'
    t.status = 'visitedByT'

    while Ls1 and Ls2:
        next_layer_s = []
        for u in Ls1:
            for v in u.getOutNeighbors():
                if v.status == 'unvisited':
                    v.status = 'visitedByS'
                    path_from_s[v] = path_from_s[u] + [v]
                    next_layer_s.append(v)
                    if v.status == 'visitedByT':
                        return path_from_s[v] + path_from_t[v][::-1]
                    
        next_layer_t = []
        for u in Ls2:
            for v in u.getInNeighbors():
                if v.status == 'unvisited':
                    v.status = 'visitedByT'
                    path_from_t[v] = path_from_t[u] + [v]
                    next_layer_t.append(v)
                    if v.status == 'visitedByS':
                        return path_from_s[v] + path_from_t[v][::-1]

        Ls1 = next_layer_s
        Ls2 = next_layer_t

    return None
