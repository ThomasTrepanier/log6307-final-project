def zipzag(fill, *cols):
   
   sizes = [len(col) for col in cols] # size of individual list in nested list
   
   longest = max(*sizes) 
   
   return [[xs[i] if i < sizes[j] else fill(xs) for j, xs in enumerate(cols)]for i in range(longest)] 

cont_det = [['TASU 117000 0', "TGHU 759933 - 0", 'CSQU3054383', 'BMOU 126 780-0', "HALU 2014 13 3"], ['40HS'], ['Ha2ardous Materials', 'Arm5 Maehinery']] 
                           

print(zipzag(lambda xs: xs[0], *cont_det))                    
