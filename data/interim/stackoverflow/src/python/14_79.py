d_level1 = {"a":1,"b":2,"c":3}
d_level2 = {"group_1":{"a":1}, "group_2":{"b":2,"c":3}}
d_level3 = {"collection_1":d_level2}

def flatten(d_in, base=()):
    for k in d_in:
        if type(d_in[k]) == dict:
            flatten(d_in[k], base+(k,))
        else:
            print(base + (k, d_in[k]))

flatten(d_level1)
# ('a', 1)
# ('b', 2)
# ('c', 3)

flatten(d_level2)
#('group_1', 'a', 1)
#('group_2', 'b', 2)
#('group_2', 'c', 3)

flatten(d_level3)
# ('collection_1', 'group_1', 'a', 1)
# ('collection_1', 'group_2', 'b', 2)
# ('collection_1', 'group_2', 'c', 3)
