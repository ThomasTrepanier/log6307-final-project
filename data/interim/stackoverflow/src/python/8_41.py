def partition(ratings):

    def helper(ratings, left, right, aux_list, current_index):
        if current_index >= len(ratings):
            aux_list.append((left, right))
            return

        first = ratings[current_index]
        helper(ratings, left + [first], right, aux_list, current_index + 1)
        helper(ratings, left, right + [first], aux_list, current_index + 1)

    #l contains all possible sublists
    l = []
    helper(ratings, [], [], l, 0)
    set1 = []
    set2 = []
    #set mindiff to a large number
    mindiff = 1000
    for sets in l:
        diff = abs(sum(sets[0]) - sum(sets[1]))
        if diff < mindiff:
            mindiff = diff
            set1 = sets[0]
            set2 = sets[1]
    return (set1, set2)
