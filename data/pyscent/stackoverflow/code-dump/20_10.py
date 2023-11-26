def __getitem__(self, i_dex, resize_=(320,480)):
        transforms_ = transforms.Compose([
                                        transforms.PILToTensor(),
                        transforms.ConvertImageDtype(torch.float32),
                                        ])
        im_ = Image_.open(self.data_paths[i_dex])
        if im_.mode !='RGB':
            im_ = im_.convert('RGB')
        im_ = im_.resize(resize_)
      
        return transforms_(im_), labels[i_dex]
