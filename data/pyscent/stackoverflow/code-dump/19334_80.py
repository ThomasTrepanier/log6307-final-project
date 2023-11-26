import re

code_string = """
# A comment.
def foo(a, b):
  return a + b
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

class Baz(object):
  def hello(self, x):
    return self.hello(
x - 1)

def my_type_annotated_function(
  my_long_argument_name: SomeLongArgumentTypeName
) -> SomeLongReturnTypeName:
  # This function's indentation isn't unusual at all.
  pass

def test_multiline():
    \"""
    asdasdada
sdadd
    \"""
    pass

def test_comment(
    a #)
):
    return [a,
    # ]
a]

def test_escaped_endline():
    return "asdad \
asdsad \
asdas"

def test_nested():
    return {():[[],
{
}
]
}

def test_strings():
    return '\""" asdasd' + \"""
12asd
12312
"asd2" [
\"""

\"""
def test_fake_def_in_multiline()
\"""
    print(123)
a = "def in_string():"
  def after().
    print("NOPE")

\"""Phew this ain't valid syntax\""" def something(): pass

""".strip()

code_string += '\n'


func_list=[]
func = ''
tab  = ''
brackets = {'(':0, '[':0, '{':0}
close = {')':'(', ']':'[', '}':'{'}
string=''
tab_f=''
c1=''
multiline=False
check=False
for line in code_string.split('\n'):
    tab = re.findall(r'^\s*',line)[0]
    if re.findall(r'^\s*def', line) and not string and not multiline:
        func += line + '\n'
        tab_f = tab
        check=True
    if func:
        if not check:
            if sum(brackets.values()) == 0 and not string and not multiline:
                if len(tab) <= len(tab_f):
                    func_list.append(func)
                    func=''
                    c1=''
                    c2=''
                    continue
            func += line + '\n'
        check = False
    for c0 in line:
        if c0 == '#' and not string and not multiline:
            break
        if c1 != '\\':
            if c0 in ['"', "'"]:
                if c2 == c1 == c0 == '"' and string != "'":
                    multiline = not multiline
                    string = ''
                    continue
                if not multiline:
                    if c0 in string:
                        string = ''
                    else:
                        if not string:
                            string = c0
            if not string and not multiline:
                if c0 in brackets:
                    brackets[c0] += 1
                if c0 in close:
                    b = close[c0]
                    brackets[b] -= 1
        c2=c1
        c1=c0

for f in func_list:
    print('-'*40)
    print(f)
