def __getitem__(self, index):

    if type(index) == torch.Tensor:
        index = index.item()

    x = torch.tensor(self.x_data.iloc[index].values, dtype=torch.float)
    y = torch.tensor(self.y_data.iloc[index], dtype=torch.float)
    return (x, y)
