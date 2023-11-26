def test_element_existed(list1, list2):
    a = set([j for i in range(len(list1)) for j in list1[i]])
    b = set([j for i in range(len(list2)) for j in list2[i]])
    #check if any element in set(a) and set(b) are common and print it
    print(bool(set(a) & set(b)), set(a) & set(b))
    return list(a.union(b) - a.intersection(b))
test_element_existed(rr, pp)
