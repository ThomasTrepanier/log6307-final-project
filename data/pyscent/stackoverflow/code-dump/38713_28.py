def gp_chris(f1, f2):
    a = f1.values.ravel()
    b, _ = pd.factorize((f2 + f2.columns).values.ravel())

    o = sparse.csr_matrix(
        (a, b, np.arange(a.shape[0] + 1)), (a.shape[0], b.max() + 1)
    ).sum(0).A1

    return pd.DataFrame(o[b].reshape(f1.shape), columns=df1.columns)


def gp_cs(f1, f2):
    return pd.concat([f1[c].groupby(f2[c]).transform('sum') for c in f1.columns], axis=1)


def gp_scott(f1, f2):
    return f1.apply(lambda x: x.groupby(f2[x.name]).transform('sum'))


def gp_wen(f1, f2):
    return f1.stack().groupby([f2.stack().index.get_level_values(level=1), f2.stack()]).transform('sum').unstack()
