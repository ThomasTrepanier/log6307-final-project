def make_dataset(dir):
    import os
    images = []
    d = os.path.expanduser(dir)

    if not os.path.exists(dir):
        print('path does not exist')

    for root, _, fnames in sorted(os.walk(d)):
        for fname in sorted(fnames):
            path = os.path.join(root, fname)
            images.append(path)
    return images    
