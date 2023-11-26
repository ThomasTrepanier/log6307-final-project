def privateNS():

    class MyObject(object):
        __slots__ = ['private'] # name doesn't matter

        def __new__(cls, value): # only sets inst.private on new instance creation
            inst = object.__new__(cls)

            setprivate(inst, value)

            return inst

        # __init__ is not needed, and can't be used here to set inst.private

        def showprivate(inst):
            return getprivate(inst)

    dsc = MyObject.private # get descriptor
    getprivate = dsc.__get__
    setprivate = dsc.__set__
    del MyObject.private # revoke normal access

    return MyObject

MyObject = privateNS()
del privateNS

inst = MyObject( 20 )
print( inst.showprivate() ) # 20
