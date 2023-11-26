url = ["www.annauniv.edu", "www.abc.co.uk", "x.dev", "x.mom", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

def myFn(x):
    order = {'edu': 0, 'com': 1, 'org': 2, 'in': 3}
    tld = x.split('.')[-1]
    return order[tld] if tld in order.keys() else tld

print(sorted(url, key=myFn))
