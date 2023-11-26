def cycles(indices):

    def get_loop(indices, idx):             # this funtion returns a loop, starting from index `idx`
        seen, loop = set(), []
        while True:
            v = indices[idx]                # get index on position `idx`
            if v not in seen:               # have we seen index `v` already?
                loop.append(idx)            # no, add it as part of the loop
                seen.add(v)                 #   update set `seen` with index `v`
                idx = v                     #   set current index `idx` with index `v`
            else:
                break                       # yes, that means we closed the loop
        return loop                         # return this loop

    rv, seen = [], set()
    for i in indices:                       # iterate over all indices
        if i not in seen:                   # is index `i` part of any loop we already have?
            loop = get_loop(indices, i)     # no, so call get_loop() with starting index `i`
            rv.append(loop)                 # we add this loop to the result list
            seen.update(loop)               # update set `seen` with all indices inside this loop

    return rv

print(cycles([2, 0, 1, 4, 3, 5]))
print(cycles([0, 1, 2, 3, 4, 5]))
print(cycles([12, 0, 8, 10, 9, 6, 5, 4, 13, 7, 17,14, 2,18, 16, 1, 11, 19, 3, 15]))
