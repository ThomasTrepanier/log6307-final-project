def f(s=None):
    def fo(s=None):
        if s==None:
            print('o',end='')
            return fo
        else:
            print(s)
            return
    if s!=None:
        print('f',end='')
        print(s)
        return
    elif s==None:
        print('fo',end='')
        return fo
