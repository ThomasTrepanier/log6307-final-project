import sys

class FakeSequence:
    def __init__(self, length_function):
        self.real_sequence = list()
        self.append = self.real_sequence.append
        self.length_function = length_function

    def __len__(self):
        return self.length_function()

if __name__ == '__main__':

    def mylen():
        return 5

    fake_sequence = FakeSequence(mylen)
    fake_sequence.append(1)
    fake_sequence.append(2)
    fake_sequence.append(3)

    length = len(fake_sequence)
    sys.stdout.write("len(fake_sequence) is %d\n" % (length))
