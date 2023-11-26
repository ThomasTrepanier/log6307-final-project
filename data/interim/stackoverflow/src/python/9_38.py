def randomize_tiles_shuffle_blocks(a, M, N):    
    m,n = a.shape
    b = a.reshape(m//M,M,n//N,N).swapaxes(1,2).reshape(-1,M*N)
    np.random.shuffle(b)
    return b.reshape(m//M,n//N,M,N).swapaxes(1,2).reshape(a.shape)
