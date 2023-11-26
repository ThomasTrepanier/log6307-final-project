import threading
import requests, json
import time
from urllib.parse import urlparse

final_dict = {} # will hold final results

def parser(u):
    try:
        parsed_uri = urlparse(u) # parse url to get domain name that'l be used as key in final_dict
        domain = "{uri.netloc}".format(uri=parsed_uri)
        x = requests.get(u)
        status_code = x.status_code
        headers = x.headers
        cookies = x.cookies
        # OR cookies = ";".join(f"{k}:{v}" for k,v in x.cookies.iteritems())
        html = x.text
        # do something with the parsed url, in this case, I created a dictionary containing info about the parsed url: timestamp, url, status_code, html, headers and cookies
        if not domain in final_dict:
            final_dict[domain] = []
        final_dict[domain].append( {'ts': time.time(), 'url': u, 'status': status_code , 'headers': str(headers), 'cookies': str(cookies), 'html': html} )

    except Exception as e:
        pass
        print(e)
        return {}

max_threads = 10
urls = ['https://google.com','https://www.facebook.com', 'https://google.com/search?q=hello+world', 'https://www.facebook.com/messages/', 'https://google.com/search?q=learn+python', 'https://www.facebook.com/me/photos', 'https://google.com/search?q=visit+lisboa', 'https://www.facebook.com/me/photos_albums']

for u in urls:
    threading.Thread(target=parser, args=[u]).start()
    tc = threading.active_count()
    while tc == max_threads:
        tc = threading.active_count()
        time.sleep(0.2)

while tc != 1: # wait for threads to finish, when tc == 1 no more threads are running apart from the main process.
    tc = threading.active_count()
    time.sleep(0.2)

print(json.dumps(final_dict))

'''
# save to file
with open("output.json", "w") as f:
    f.write(json.dumps(final_dict))

# load from file
with open("output.json") as f:
    _json = json.loads(f.read())
'''
