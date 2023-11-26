def par_nepar(n):
    cifre = list(str(n))
    flg = False
    if int(cifre[0]) % 2 == 0:
        flg = True
    for d in cifre[1:]:
        _flg = False
        if int(d) % 2 == 0:
            _flg = True
        if not flg^_flg:
            print("The number does not complies to the needed terms")
            return
        flg = _flg
    print("The number complies to the needed terms")
    return
