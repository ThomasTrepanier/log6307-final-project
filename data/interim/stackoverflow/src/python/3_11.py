def scanner2(path, input):
    with open(path) as file:
         lines = file.readlines()
         for index, line in enumerate(lines):
             if line[1].isdigit() == True and line[22: -13].strip(" ") == input:
                 print(line)
                 lin = index+1
                 try:
                     while lines[lin][1].isdigit() is False:
                         print(lines[lin])
                         lin +=1
                 except IndexError:
                     break


print("="*40)
print(f"*****History of {inp}*****")        
scanner2(path2, inp)
