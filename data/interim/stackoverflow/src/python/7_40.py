def find_ISIN(S):
    ISIN_list = []
    for i in range(len(S) - 12):
        if S[i:i+2].isalpha() and S[i+2:i+12].isdigit():
            ISIN_list.append(S[i:i+12])    
    return ISIN_list
