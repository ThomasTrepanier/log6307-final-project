from types import SimpleNamespace


def parse(data):
    if type(data) is list:
        return list(map(parse, data))
    elif type(data) is dict:
        sns = SimpleNamespace()
        for key, value in data.items():
            setattr(sns, key, parse(value))
        return sns
    else:
        return data


info = {
    'country': 'Australia',
    'number': 1,
    'slangs': [
        'no worries mate',
        'winner winner chicken dinner',
        {
            'no_slangs': [123, {'definately_not': 'hello'}]
        }
    ],
    'tradie': {
        'name': 'Rizza',
        'occupation': 'sparkie'
    }
}

d = parse(info)
assert d.country == 'Australia'
assert d.number == 1
assert d.slangs[0] == 'no worries mate'
assert d.slangs[1] == 'winner winner chicken dinner'
assert d.slangs[2].no_slangs[0] == 123
assert d.slangs[2].no_slangs[1].definately_not == 'hello'
assert d.tradie.name == 'Rizza'
assert d.tradie.occupation == 'sparkie'
