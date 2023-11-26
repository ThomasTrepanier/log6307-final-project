code_string = """
#A comment
def foo(a, b):
  return a + b

def bir(a, b):
  c = a + b
  return c

class Bar(object):
  def __init__(self):
    self.my_list = [
        'a',
        'b',
    ]

def baz():
  return [
1,
  ]

""".strip()

lines = code_string.split('\n')

#looking for lines with 'def' keywords
defidxs = [e[0] for e in enumerate(lines) if 'def' in e[1]]

#getting the indentation of each 'def'
indents = {}
for i in defidxs:
    ll = lines[i].split('def')
    indents[i] = len(ll[0])

#extracting the strings
end = len(lines)-1
while end > 0:
    if end < defidxs[-1]:
        defidxs.pop()
    try:
        start = defidxs[-1]
    except IndexError: #break if there are no more 'def'
        break

    #empty lines between functions will cause an error, let's remove them
    if len(lines[end].strip()) == 0:
        end = end -1
        continue

    try:
        #fix lines removing indentation or compile will not compile
        fixlines = [ll[indents[start]:] for ll in lines[start:end+1]] #remove indentation
        body = '\n'.join(fixlines)
        compile(body, '<string>', 'exec') #if it fails, throws an exception
        print(body)
        end = start #no need to parse less line if it succeed.
    except:
        pass

    end = end -1
