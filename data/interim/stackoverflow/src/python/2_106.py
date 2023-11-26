from urllib.request import urlopen
from urllib.parse import urlencode
from json import loads


def getJSON(page):
    params = urlencode({
        'format': 'json',
        'action': 'parse',
        'prop': 'text',
        'redirects' : 'true',
        'page': page})
    API = "https://en.wikipedia.org/w/api.php"
    response = urlopen(API + "?" + params)
    return response.read().decode('utf-8')


def getRawPage(page):
    parsed = loads(getJSON(page))
    try:
        title = parsed['parse']['title']
        content = parsed['parse']['text']['*']
        return title, content
    except KeyError:
        # The page doesn't exist
        return None, None

title, content = getRawPage("Mathematics")
