def plot_network(nodes, edges):
    x_values = []
    y_values = []

    for node, connected_nodes in edges.items():
        for connected_node in connected_nodes:
            x_values.extend([nodes.index(node), nodes.index(connected_node), None])
            y_values.extend([nodes.index(connected_node), nodes.index(node), None])

    edge_trace = go.Scatter(
        x=x_values,
        y=y_values,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    # Continue from here with the rest of your code...
