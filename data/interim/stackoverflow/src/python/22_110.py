def process_cursor(G, passed, node_id):
    if set(G.predecessors(node_id)).issubset(passed):
        return True, list(G.successors(node_id))
    return False, None


def get_all_roots(G: nx.DiGraph):
    for node_id in G.nodes:
        if not any(G.predecessors(node_id)):
            yield node_id


def order_components(G: nx.DiGraph):
    nodes_amount = len(G.nodes)
    cursors = set(get_all_roots(G))
    passed = []
    iterations = 0
    while len(passed) != nodes_amount:
        iterations += 1
        if iterations > nodes_amount:
            raise ValueError("Could not create sequence of graph.")
        step = []
        next_cursors = []
        step_passed = []
        for node_id in cursors:
            can_process, tmp_cursors = process_cursor(G, passed, node_id)
            if can_process:
                next_cursors.extend(tmp_cursors)
                step_passed.append(node_id)
                node_data = G.nodes[node_id]
                step.append(node_id)
        cursors = set(next_cursors)
        passed.extend(step_passed)
        if step:
            yield step
    yield append
