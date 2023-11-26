import itertools as it

def splitter(seq):                                                             
    temp = [seq]
    for x in range(1, len(seq)):
        print(seq[:x], seq[x:])
        temp.append(seq[:x])
        temp.append(seq[x:])
    return temp

if __name__ == "__main__":
    test = input("Enter a string: ")
    temp = splitter(test)
    copy = temp[::]
    condition = True
    for x in temp:
        if len(x) > 1:
            copy.extend(splitter(x))
    copy = sorted(list(set(copy)))
    print(copy)
    count = []
    for x in range(len(test)):
        item = it.permutations(copy, x)
        try:
            while True:
                temp = next(item)
                if "".join(list(temp)) == test:
                    if len(temp) == len(set(temp)):
                        count.append((len(temp), temp))
        except StopIteration:
            print('next permutation begin iteration')
            continue
    print(f"All unique splits: {count}")
    print(f"Longest unique split : {max(count)[0]}")
