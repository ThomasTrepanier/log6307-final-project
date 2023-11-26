class ImageFolder(Dataset):
    def __init__(self, root, transform=None):
        #Call make_dataset to collect files. 
        self.samples = make_dataset(opt.dataroot)
        self.imgs = self.samples
        self.transformA = transformA

        ...
