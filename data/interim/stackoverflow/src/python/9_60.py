def bin_rep(A,n):
    if n in (8,16,32,64):
        return (np.unpackbits(A.astype(f'>u{n>>3}').view(np.uint8))+ord('0')).view(f'S{n}')
    nb = max((n-1).bit_length()-3,0)
    return (np.unpackbits(A.astype(f'>u{1<<nb}')[...,None].view(np.uint8),axis=1)[...,-n:]+ord('0')).ravel().view(f'S{n}')
