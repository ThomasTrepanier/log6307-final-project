def mergeArys(srtd_arys):
    heap = []
    srtd_iters = [iter(x) for x in srtd_arys]

    # put the first element from each srtd array onto the heap
    for idx, it in enumerate(srtd_iters):
        elem = next(it, None)
        if elem:
            heapq.heappush(heap, (elem, idx))

    res = []

    # collect results in nlogK time
    while heap:
        elem, ary = heap[0]
        lowest = elem
        keep_elem = True
        for i in range(len(srtd_arys)):
            elem, ary = heap[0]
            if lowest != elem or ary != i:
                if ary != i:
                    heapq.heappop(heap)
                    it = srtd_iters[ary]
                    nxt = next(it, None)
                    if nxt:
                        heapq.heappush(heap, (nxt, ary))

                keep_elem = False
                i -= 1
                break
            heapq.heappop(heap)

        if keep_elem:
            res.append(elem)

        for unbenched in range(i+1):
            unbenched_it = srtd_iters[unbenched]
            nxt = next(unbenched_it, None)
            if nxt:
                heapq.heappush(heap, (nxt, unbenched))

        if len(heap) < len(srtd_arys):
            heap = []

    return res

