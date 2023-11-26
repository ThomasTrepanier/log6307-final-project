def whatistheremainder(v):
    first, sep, rest = v.partition(' ')
    return rest if sep else first

for s in ['the quick brown fox', 'hi there', 'single', '', 'abc\tefg']:
    whatistheremainder(s)

'quick brown fox'
'there'
'single'
''
'abc\tefg'
