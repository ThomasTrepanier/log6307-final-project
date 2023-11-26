pos_test_data = [5678, 901, 9012, 9012345678901]
neg_test_data = [5876, 910, 9021]

def monotonic_by_one(n):
    fwd = str(n)
    tgt = ord(fwd[0]) + ord(fwd[-1])
    return all([ord(f) + ord(r) in (tgt, tgt - 10) for f, r in zip(fwd, reversed(fwd))])


print("Positive: ", all([monotonic_by_one(n) for n in pos_test_data]))
print("Negative: ", all([not monotonic_by_one(n) for n in neg_test_data]))
