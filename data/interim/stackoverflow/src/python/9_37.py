def randomize_tiles_shuffle_within(a, M, N):
    # M,N are the height and width of the blocks
    m,n = a.shape
    b = a.reshape(m//M,M,n//N,N).swapaxes(1,2).reshape(-1,M*N)
    np.random.shuffle(b.T)
    return b.reshape(m//M,n//N,M,N).swapaxes(1,2).reshape(a.shape)
