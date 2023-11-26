class SingleCharReplacingFilter:

    def __init__(self, reader, oldchar, newchar):
        def proxy(obj, attr):
            a = getattr(obj, attr)
            if attr in ('read'):
                def f(*args):
                    return a(*args).replace(oldchar, newchar)
                return f
            else:
                return a

        for a in dir(reader):
            if not a.startswith("_") or a == '__iter__':
                setattr(self, a, proxy(reader, a))

def csv_reader_6(x):
    with x as fin:
        return pd.read_csv(SingleCharReplacingFilter(fin, ";", ","),
                            sep=',', header=None, usecols=[3, 4, 5])
