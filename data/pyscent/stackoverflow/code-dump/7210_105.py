class myList(list):
    def in_other(self, other_list):
        for i in range(0, len(other_list)-len(self)):
            if other_list[i:i+len(self)] == self:
                return True
            else:
                continue

if __name__ == "__main__":

    x = myList([1, 2, 3])
    b = [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

    print(x.in_other(b))
