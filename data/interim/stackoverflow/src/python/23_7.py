def zip_first(first, second, third, fillvalue=None):
    filler = repeat(fillvalue)
    return zip(first,
               chain(second, filler),
               chain(third, filler))
