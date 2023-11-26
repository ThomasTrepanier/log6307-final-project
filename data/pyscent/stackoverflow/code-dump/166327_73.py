import random


def foo(n, low, high):
    """Helper function for recursive function"""

    def rbar(arr):
        """Recursive function to create a 'random' list of n integers
        between low and high (exclusive) such that the sum of the list is 0
        and the entries of the list are unique."""

        # if one spot left check if -sum(arr) in arr
        if len(arr) == n-1:
            if -sum(arr) not in arr and -sum(arr) in range(low, high):
                    return arr + [-sum(arr)]

        # if more than one spot then generate the next possible values
        # and try to get to a full list of size n with those
        else:
            # loop through shuffled options (randomness here)
            options = [x for x in range(low, high) if x not in arr]

            for opt in random.sample(options, len(options)):
                # if recursively going through function produces a list then return it
                if rbar(arr + [opt]) is not None:
                    return rbar(arr + [opt])

            # if nothing worked then return None
            return


    if n==0:
        return []
    elif n==1 and 0 in range(low, high):
        return [0]
    elif n==1 and 0 not in range(low, high):
        return None
    else:
        return rbar([])


k = foo(4, -10, 10)

if k is not None:
    print("List: {}, Sum:{}".format(k, sum(k)))
else:
    print(None)
