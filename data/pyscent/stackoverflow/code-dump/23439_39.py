from skimage.util import view_as_blocks

def shuffle_tiles(arr, m, n):
    a_= view_as_blocks(arr,(m,n)).reshape(-1,m,n)
    # shuffle works along 1st dimension and in-place
    np.random.shuffle(a_)
    return a_
