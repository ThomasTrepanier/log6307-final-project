def connections(graph, id):
    def dict_to_df(d):
        df = pd.DataFrame(data=[d.keys(), d.values()], index=['ID', 'Subgraph']).T
        df['id'] = id
        return df[['id', 'Subgraph', 'ID']]

    def dfs(node, num):
        visited[node] = num
        for _node in graph.loc[node].iloc[0]:
            if _node not in visited:
                dfs(_node, num)

    visited = {}
    graph = graph.loc[id]
    for (num, node) in enumerate(graph.index):
        if node not in visited:
            dfs(node, num)

    return dict_to_df(visited)

dfs = []
for id in graph.index.get_level_values(0).unique():
    dfs.append(connections(graph, id))

conns = pd.concat(dfs)
