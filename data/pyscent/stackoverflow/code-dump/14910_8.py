import json
from collections import Counter, defaultdict

data = """{"Date": "Fri, 19 Apr 2019 00:54:46 GMT", "Vary": "Host,Accept-Encoding", "Key-Word": "00a", "Cache-Control": "private", "Key-Word": "xn"}

"""

def duplicate_keys(pairs):
    out = {}
    dups = defaultdict(list)
    key_count = Counter(key for key, value in pairs)

    for key, value in pairs:
        if key_count[key] == 1:
            out[key] = value
        else:
            dups[key].append(value)

    # Concatenate the lists of values in a string, enclosed in {} and separated by ';'
    # rather than in a list:       
    dups = {key: ';'.join('{' + v + '}' for v in values) for key, values in dups.items()}

    out.update(dups)
    return out

decoded = json.loads(data, object_pairs_hook=duplicate_keys)
print(decoded)

# {'Date': 'Fri, 19 Apr 2019 00:54:46 GMT', 
#  'Vary': 'Host,Accept-Encoding', 
#  'Cache-Control': 'private', 
#  'Key-Word': '{00a};{xn}'}
