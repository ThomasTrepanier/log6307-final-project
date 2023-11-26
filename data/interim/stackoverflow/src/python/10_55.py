import sys

def getsizeof_dict_literal(n):
    pairs = ["{0}:{0}".format(i) for i in range(n)]
    dict_literal = "{%s}" % ", ".join(pairs)
    source = "sys.getsizeof({})".format(dict_literal)
    size = eval(source)
    return size
