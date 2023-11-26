def test_lbom():
    '''
    >>> from lbom import *
    >>> random.seed(1234)
    >>> test = Lbom(color='blue', combo = 3.4)
    color: blue
    336.59999999999997
    >>> test.print_color('red')
    color: red
    >>> random.seed(1010)
    >>> test.combo(-1)
    -85
    >>>
    '''


if __name__ == '__main__':
  import doctest
  doctest.testmod(name='test_lbom', verbose=True)
