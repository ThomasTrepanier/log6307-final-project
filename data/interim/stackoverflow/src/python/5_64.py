def readAndWriteFile(read_file_path,write_file_path):
    with open(read_file_path,"r") as fin:
        output = [", ".join(element.split(',')) for element in fin.readlines()]
    print("output:",output)
    
    with open(write_file_path,'w') as fout:
        fout.writelines(output)
