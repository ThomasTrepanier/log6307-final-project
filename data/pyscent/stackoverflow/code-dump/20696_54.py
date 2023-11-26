category_cases = {'weather': ['windy', 'calm'],
                  'season': ['summer', 'winter', 'spring', 'autumn'],
                  'lateness': ['ontime', 'delayed']}
order = ['weather', 'season', 'lateness']

def gen_tree(category_cases, order):
    if len(order) == 0:
        return 0
    return {x:gen_tree(category_cases, order[1:]) for x in category_cases[order[0]]}
