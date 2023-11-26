def __init__(self):
    super(MyModel, self).__init__()
    self.layer1 = nn.Linear(10, 20)
    self.layer2 = nn.Linear(20, 5)
    self.relu = nn.ReLU()
