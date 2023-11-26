def select_min(x):
    m = x['value'].min()
    if len(x) > 1 and (x['value'] == m).all():
        return -1
    else:
        return x['value'].idxmin()

selected = data.groupby(['id', 'Subgraph'])['value', 'ID'].apply(select_min)
selected = selected[selected >= 0]
