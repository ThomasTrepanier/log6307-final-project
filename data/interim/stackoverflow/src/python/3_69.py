class MyList:
    def __init__(self,list):
        self.list=list

    def __setitem__(self, i, elem):
        self.list[i] = elem
