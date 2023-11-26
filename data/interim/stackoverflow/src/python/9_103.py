def get(str,target_index):
  start = len(" ".join(str.split(" ")[:target_index])) + 1
  end = start + len(str.replace('.','').split(' ')[target_index])
  return (start,end)

str = 'cold weather gives me cold.' 
tag = ['O','O','O','O','disease']
start,end = get(str,tag.index('disease'))
print(start,end,str[start:end]) # outputs 22 26 cold

str = 'cold weather gives me cold'
tag = ['O','O','O','O','disease']
start,end = get(str,tag.index('disease'))
print(start,end,str[start:end]) # outputs 22 26 cold

str = 'cold weather gives me cold and cough' 
tag = ['O','O','O','O','disease']
start,end = get(str,tag.index('disease'))
print(start,end,str[start:end]) # outputs 22 26 cold
