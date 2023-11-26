url = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', 'www.website.org', 'www.bis.org.in', 'www.rbi.org.in']

def topLevelDomain(domain: str):
    # Split from the right, max of one split.
    # This only takes the right hand side after the last period in the string.
    return domain.rsplit('.', 1)[-1]

print(sorted(url, key=topLevelDomain))
