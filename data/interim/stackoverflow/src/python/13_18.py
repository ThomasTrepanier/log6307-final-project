def uniqifyColors(l):
    for elem in l:
        for item in l:
            if elem['number'] == item['number'] and elem['favorite'] == item['favorite']:
                for clr in item['color']:
                    if clr not in elem['color']:
                        elem['color'].append(clr)
    return l
