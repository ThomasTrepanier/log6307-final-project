class AnyList(object):
    def __init__(self, *args, **kwargs):
        self.mylength = 0

    def __len__(self, *args, **kwargs): # len()
        return self.mylength

    def append(self):
        self.mylength += 1

if __name__ == '__main__':
    fake_sequence = AnyList()
    fake_sequence.append()
    fake_sequence.append()

    print("len(AnyList) is %d" % len(fake_sequence))
    # reads out 2
