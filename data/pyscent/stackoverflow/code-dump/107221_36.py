import traceback, ast, re
def get_fun(name, ast_obj):
    if isinstance(ast_obj, ast.Call) and ast_obj.func.id == name:
        yield from [i.arg for i in getattr(ast_obj, 'keywords', [])]
    for a, b in getattr(ast_obj, '__dict__', {}).items():
        yield from (get_fun(name, b) if not isinstance(b, list) else \
                        [i for k in b for i in get_fun(name, k)])

def passed_positionally(stack):
    *_, [_, co], [trace, _] = [re.split('\n\s+', i.strip()) for i in stack] 
    f_name = re.findall('(?:line \d+, in )(\w+)', trace)[0]
    return list(get_fun(f_name, ast.parse(co)))

def foo(x, y):
    if 'y' in passed_positionally(traceback.format_stack()):
        print('y was passed with its keyword')
    else:
        print('y was passed positionally')

foo(1, y=2)
