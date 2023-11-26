inp = input("please, Enter your input that you want to search for: ")


def scanner (path, input):
    with open(path) as file:
         lines = file.readlines()
         for index, line in enumerate(lines):
             if line[0].isdigit() == True and line[20: -13] == input:
                 print(line)
                 lin = index+1
                 try:
                     while lines[lin][0].isdigit() is False:
                         print(lines[lin])
                         lin +=1
                 except IndexError:
                     break

print("="*40)
print(f"*****History of {inp}*****")        
scanner(path, inp)
