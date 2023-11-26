def nametag(first_name, last_name):
    name = '{}.{}'.format(first_name, last_name)
    location = name.find('.')
    name = name[:location + 2].replace('.', ' ') + '.'
    return name
