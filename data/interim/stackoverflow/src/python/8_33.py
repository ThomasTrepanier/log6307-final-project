def front_back(val):
    if len(val) <= 1:
        return val

    return val[-1] + val[1:-1] + val[0]


print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
