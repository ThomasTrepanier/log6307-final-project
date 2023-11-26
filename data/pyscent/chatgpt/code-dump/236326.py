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

    node_trace = go.Scatter(
        x=[nodes.index(node) for node in nodes],
        y=[nodes.index(node) for node in nodes],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))

    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title='<br>Network graph',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    fig.show()
