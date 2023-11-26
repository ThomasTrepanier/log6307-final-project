def serge(frame):
    contains = [frame['a'].str.contains(i) for i in letters]
    return frame[np.all(contains, axis=0)]

def yatu(frame):
    letters_s = set(letters)
    return frame[frame.a.str.split(',').map(letters_s.issubset)]

def austin(frame):
    mask =  frame.a.apply(lambda x: np.intersect1d(x.split(','), letters).size > 0)
    return frame[mask]

def datanovice(frame):
    s = frame['a'].str.split(',').explode().isin(letters).groupby(level=0).cumsum()
    return frame.loc[s[s.ge(2)].index.unique()]

perfplot.show(
    setup=lambda n: pd.concat([frame]*n, axis=0).reset_index(drop=True), 

    kernels=[
        lambda df: serge(df),
        lambda df: yatu(df),
        lambda df: df[df['a'].apply(lambda x: np.all([*map(lambda l: l in x, letters)]))],
        lambda df: austin(df),
        lambda df: datanovice(df),
    ],

    labels=['serge', 'yatu', 'bruno','austin', 'datanovice'],
    n_range=[2**k for k in range(0, 18)],
    equality_check=lambda x, y: x.equals(y),
    xlabel='N'
)
