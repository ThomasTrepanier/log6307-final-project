from pprint import pprint

l = [{'name': 'jamie', 'age': 26, 'color': 'gold'},
     {'name': 'tara', 'age': 43, 'hobby': 'archery'},
     {'name': 'matt', 'age': 34, 'epic': 'louhi'}
]

def compile(ls):
    dx = dict()
    for d in ls:
        for k, v in d.items():
            current = dx.get(k, [])  # Leverage get() default value option 
            current.append(v)
            dx[k] = current
    return dx

result = compile(l)
pprint(result)
