def plot_network(nodes, edges):
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    for node, connected_nodes in edges.items():
        for connected_node in connected_nodes:
            edge_trace['x'].extend([nodes.index(node), nodes.index(connected_node), None])
            edge_trace['y'].extend([nodes.index(connected_node), nodes.index(node), None])

    # Rest of your code...
