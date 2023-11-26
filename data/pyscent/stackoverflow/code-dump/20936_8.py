from backoff_utils import backoff, apply_backoff, strategies

@apply_backoff(strategies.Fixed, max_tries = 3, catch_exceptions = [type(ValueError)])
def main2():
    # np.load('File2.csv')
    raise ValueError
    print("In main2")
