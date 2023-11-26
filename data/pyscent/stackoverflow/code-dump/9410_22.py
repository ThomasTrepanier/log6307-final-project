d = {
    "Name1": {
        "NNum": "11",
        "Node1": {
            "SubNodeA": "Thomas",
            "SubNodeB": "27"
        },
        "Node2": {
            "SubNodeA": "ZZZ",
            "SubNodeD": "XXX",
            "SubNodeE": "yy"
        },
        "Node3": {
                "child1": 11,
                "child2": {
                    "grandchild": {
                        "greatgrandchild1": "Rita",
                        "greatgrandchild2": "US"
                                }
                            }
                }
            }
}

def get_keys(d, curr_key=[]):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from get_keys(v, curr_key + [k])
        elif isinstance(v, list):
            for i in v:
                yield from get_keys(i, curr_key + [k])
        else:
            yield '.'.join(curr_key + [k])

print([*get_keys(d)])
