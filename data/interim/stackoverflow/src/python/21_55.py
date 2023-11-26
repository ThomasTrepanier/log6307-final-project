import heapq


def mergeArys(srtd_arys):
    heap = []
    srtd_iters = [iter(x) for x in srtd_arys]

    # put the first element from each srtd array onto the heap
    for idx, it in enumerate(srtd_iters):
        elem = next(it, None)
        if elem:
            heapq.heappush(heap, (elem, idx))

    res = []

    # the number of tims that the current number has been seen
    times_seen = 0

    # the lowest number from the heap - currently checking if the first numbers in all sub-lists are equal to this
    lowest = heap[0][0] if heap else None

    # collect results in nlogK time
    while heap:
        elem, ary = heap[0]
        unbench_all = True

        if lowest != elem or ary != times_seen:
            if lowest == elem:
                heapq.heappop(heap)
                it = srtd_iters[ary]
                nxt = next(it, None)
                if nxt:
                    heapq.heappush(heap, (nxt, ary))
        else:
            heapq.heappop(heap)
            times_seen += 1

            if times_seen == len(srtd_arys):
                res.append(elem)
            else:
                unbench_all = False

        if unbench_all:
            for unbenched in range(times_seen):
                unbenched_it = srtd_iters[unbenched]
                nxt = next(unbenched_it, None)
                if nxt:
                    heapq.heappush(heap, (nxt, unbenched))
            times_seen = 0
            if heap:
                lowest = heap[0][0]

    return res


if __name__ == '__main__':
    a1 = [[1, 3, 5, 7], [1, 1, 3, 5, 7], [1, 4, 7, 9]]
    a2 = [[1, 1], [1, 1, 2, 2, 3]]
    for arys in [a1, a2]:
        print(mergeArys(arys))
