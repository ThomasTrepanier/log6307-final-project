def myFn(s):
    preferred_order = ["edu", "com", "org", "in"]
    tld=s.split('.')[-1]
    try:
        ranking = preferred_order.index(tld)
    except ValueError:
        ranking = 99999 # to sort unknowns at end; use -1 to sort at beginning 
    return ranking
