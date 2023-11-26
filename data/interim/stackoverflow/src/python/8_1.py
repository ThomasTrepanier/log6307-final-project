def my_round(n):
    lower = (n//5)*5;
    upper = lower+5;

    if (n-lower)<(upper-n):
        return int(lower)
    return int(upper)

print(my_round(703.021))
