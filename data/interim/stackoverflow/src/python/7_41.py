def find_ISIN(S):
    ISIN_list = []
    i = 0
    while i <= len(S) - 12:
        if S[i:i+2].isalpha() and S[i+2:i+12].isdigit():
            ISIN_list.append(S[i:i+12])
            i += 12
        else:
            i += 1
    return ISIN_list
