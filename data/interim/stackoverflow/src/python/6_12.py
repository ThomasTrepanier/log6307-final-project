f_name = "file.txt"
text = "102"
def check_in_file(file_name, value):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if value in line:
                return True
    return False
if check_in_file(f_name, text):
    print('Yes, string found in file')
else:
    print('String not found in file')
    file = open(f_name, 'a')
    file.write("\n"+text)
    file.close()
