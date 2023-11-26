path = 'extractiondata.txt'

def scanner(path, input):
    with open(path) as file:
        lista  = file.readlines()
        for index, each in enumerate(lista):
            if each[20:-13] == input:
                print(each)
                print(lista[index+1])
                print(lista[index+2])                
        

inp = input("please, Enter your input that you want to search for: ")                  
scanner(path, inp)


