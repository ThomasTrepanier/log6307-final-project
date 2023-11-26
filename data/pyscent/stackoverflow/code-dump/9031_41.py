def newtons_method(num, estimate):
    # Computing a new_estimate
    new_estimate = (estimate + num/estimate) / 2
    print(new_estimate)
    # Base Case: Comparing our estimate with built-in functions value
    if new_estimate == math.sqrt(num):
        return True
    else:
        return newtons_method(num, new_estimate)
