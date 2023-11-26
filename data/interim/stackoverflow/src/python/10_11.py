import re

meetingStrings = [
        "appointment",
        "meet",
        "interview"
]
text = "Fix me a meeting in 2 days"

def split_string(text, strings):
    search = re.compile('|'.join(strings))
    start = None
    input = text.split()
    for e, x in enumerate(input):
        if search.search(x):
            if start < e:
                yield ' '.join(input[start:e])
            start = None
        else:
            if start is None:
                start = e
    else:
        if start is not None:
            yield ' '.join(input[start:])

print(' '.join(split_string(text, meetingStrings)))
