from decimal import Decimal
def exact_add(*nbs):
    return float(sum([Decimal(str(nb)) for nb in nbs]))

exact_add(0.1, 0.2)
# > 0.3
