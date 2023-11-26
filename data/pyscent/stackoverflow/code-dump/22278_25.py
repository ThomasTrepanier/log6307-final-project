import sys

class FakeSequence(list):
    def __init__(self, *args, **kwargs):
        # not really necessary, leave out __init__ method, if
        # you don't have own attributes in your class.
        # but if you define an __init__ method, you
        # MUST call baseclass.__init__ inside, preferably
        # on top of the __init__ method
        list.__init__(self, *args, **kwargs)

    def __len__(self, *args, **kwargs):
        len_of_fakesequence = list.__len__(self, *args, **kwargs)
        # here you can do anything about len()
        return len_of_fakesequence

if __name__ == '__main__':
    fake_sequence = FakeSequence()
    fake_sequence.append(1)
    fake_sequence.append(2)
    fake_sequence.append(3)

    length = len(fake_sequence)
    sys.stdout.write("len(fake_sequence) is %d\n" % (length))
