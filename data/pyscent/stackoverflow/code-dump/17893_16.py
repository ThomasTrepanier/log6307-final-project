class index:
    def __init__(self, seq):
        self.seq = seq
    def __getitem__(self, boolseq):
        return [x for x, y in zip(boolseq, self.seq) if y]
print(index(a)[b])
