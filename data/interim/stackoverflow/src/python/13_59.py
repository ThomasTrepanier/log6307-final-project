def flat(lst, res = None):
  if res == None: res = []
  for item in lst:
    if not type(item) == list: res.append(item['name'])
    else: flat(item, res)
  return res

print(flat(list_of_interest))
#=> ['Viscozyme', 'Davictrel', 'Enbrel Sureclick', 'Tunex', 'Angiox', 'Enantone', 'Leuplin', 'LeuProMaxx', 'Leupromer', 'Lutrate', 'Memryte', 'Prostap 3', 'Prostap SR', 'Viadur', 'Geref']
