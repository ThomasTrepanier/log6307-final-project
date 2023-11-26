import ast

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
""".strip()

code_lines = code_string.splitlines(keepends=True)
for node in ast.walk(ast.parse(code_string)):
    if isinstance(node, ast.FunctionDef):
        lines = code_lines[node.lineno - 1:node.end_lineno]
        lines[0] = lines[0][node.col_offset:]
        lines[-1] = lines[-1][:node.end_col_offset]
        print(''.join(lines))
