# Divakar
def f_dv(a,bs):
    M,N = bs
    m,n = a.shape
    b = a.reshape(m//M,M,n//N,N).swapaxes(1,2).reshape(-1,M*N)
    np.random.shuffle(b)
    return b.reshape(m//M,n//N,M,N).swapaxes(1,2).reshape(a.shape)

from skimage.util import view_as_blocks

# Brenlla shape fixed by pp
def f_br(arr,bs):
    m,n = bs
    a_= view_as_blocks(arr,(m,n))
    sh = a_.shape
    a_ = a_.reshape(-1,m,n)
    # shuffle works along 1st dimension and in-place
    np.random.shuffle(a_)
    return a_.reshape(sh).swapaxes(1,2).reshape(arr.shape)

ex = np.arange(100000).reshape(1000,100)
bs = 10,10
tst = np.tile(np.arange(np.prod(bs)).reshape(bs),np.floor_divide(ex.shape,bs))

from timeit import timeit
for n,f in list(globals().items()):
    if n.startswith('f_'):
        assert (tst==f(tst,bs)).all()
        print(n[2:],timeit(lambda:f(ex,bs),number=1000))
