def f(s=None):
    if s: return f'f{s}'

    def factory(prefix):
        def inner(s=None):
            return f'f{prefix}{s}' if s else factory(prefix + 'o')
        return inner
    return factory('o')
