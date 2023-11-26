def list_index(p):
    for x in p:
        if x > 18:
            return p[np.where(p==x)[0][0]:]
    return []

perfplot.show(
    setup=lambda n: np.hstack([np.random.randint(0,15,10*n), np.random.randint(-20,30,10*n)]),
    kernels=[it_dropwhile, walrus, explicit_loop, genexpr_next, np_argmax, pd_idxmax, list_index, lazy_iter],
    labels=['it_dropwhile','walrus','explicit_loop','genexpr_next','np_argmax','pd_idxmax', 'list_index', 'lazy_iter'],
    n_range=[2 ** k for k in range(18)],
    equality_check=np.allclose,
    xlabel='~n/20'
)
