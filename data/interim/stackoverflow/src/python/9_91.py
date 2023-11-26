def strip_read(file):
    return file.readline().rstrip()

in_a_not_b = []
in_b_not_a = []
with open("fileA") as A:
    with open("fileB") as B:
        Aline = strip_read(A)
        Bline = strip_read(B)
        while Aline or Bline:
            if Aline < Bline and Aline:
                in_a_not_b.append(Aline)
                Aline = strip_read(A)
            elif Aline > Bline and Bline:
                in_b_not_a.append(Bline)
                Bline = strip_read(B)
            else:
                Aline = strip_read(A)
                Bline = strip_read(B)

print("in A not in B", in_a_not_b, "\nin B not in A", in_b_not_a)
