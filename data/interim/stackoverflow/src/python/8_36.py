try:
    basestring_ = basestring
except (NameError,) as e:
    basestring_ = str

try:
    cmp_ = cmp
except (NameError,) as e:
    # from http://portingguide.readthedocs.io/en/latest/comparisons.html
    def cmp_(x, y):
        """
        Replacement for built-in function cmp that was removed in Python 3
        """
        return (x > y) - (x < y)

