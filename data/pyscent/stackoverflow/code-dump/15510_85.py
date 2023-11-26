class AhoNode(object):
    def __init__(self):
        self.goto = {}
        self.is_match = False
        self.fail = None

def aho_create_forest(patterns):
    root = AhoNode()
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.is_match = True
    return root

def aho_create_statemachine(patterns):
    root = aho_create_forest(patterns)
    queue = []
    for node in root.goto.itervalues():
        queue.append(node)
        node.fail = root
    while queue:
        rnode = queue.pop(0)
        for key, unode in rnode.goto.iteritems():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.is_match = unode.is_match or unode.fail.is_match
    return root

def aho_any_match(s, root):
    node = root
    for i, c in enumerate(s):
        while node is not None and c not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[c]
        if node.out:
            return True
    return False

def all_any_matcher(*pattern_lists):
    ''' Returns an efficient matcher function that takes a string
    and returns True if at least one pattern from each pattern list
    is found in it.
    '''
    machines = [aho_create_statemachine(patterns) for patterns in pattern_lists]

    def matcher(text):
        return all(aho_any_match(text, m) for m in machines)
    return matcher
