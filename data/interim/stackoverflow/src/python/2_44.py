import re

def get_numbers(texto):
    return int(re.findall(r'[0-9]+', texto)[0])
        
def sort_list(l):
    dicto = {}
    for i in l:
        dicto[get_numbers(i)] = i
    lista = []
    for i in sorted(list(dicto.keys())):
        lista.append(dicto[i])
    return lista

sort_list(frames)
