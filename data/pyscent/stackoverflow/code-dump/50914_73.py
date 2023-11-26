from re import sub

def to_camelcase(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "").replace("*","")
  return ''.join([s[0].lower(), s[1:]])

print(to_camelcase('some_string_with_underscore'))
print(to_camelcase('Some string with Spaces'))
print(to_camelcase('some-string-with-dashes'))
print(to_camelcase('some string-with dashes_underscores and spaces'))
print(to_camelcase('some*string*with*asterisks'))
