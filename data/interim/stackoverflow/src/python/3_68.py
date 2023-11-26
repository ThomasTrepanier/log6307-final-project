class MyList:
    def __init__(self,list):
        self.list=list

    def __getitem__(self, index):
        return self.list[index]
    
    def __setitem__(self, index, value):
        self.list[index] = value
