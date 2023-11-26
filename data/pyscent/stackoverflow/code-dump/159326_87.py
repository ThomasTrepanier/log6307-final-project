urls = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

def key_function(s):
    # Turn "www.google.com" into ["www", "google", "com"], then
    # reverse it to ["com", "google", "www"].
    return list(reversed(s.split('.')))

# Now this will sort ".com" before ".edu", "google.com" before "ndtv.com",
# and so on.
print(sorted(urls, key=key_function))
