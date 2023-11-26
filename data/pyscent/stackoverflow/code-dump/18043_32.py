def procedures(txt1, txt2):
    seq1 = list(txt1.lower())
    seq2 = list(txt2.lower())

    seq1.sort()
    seq2.sort()

    if seq1 == seq2:
        return True
    else:
        return False
