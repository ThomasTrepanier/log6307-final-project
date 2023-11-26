old_list= ['list4','this1','my3','is2']
def extract_number(string):
    digits = ''.join([c for c in string if c.isdigit()])
    return int(digits)
    
new_list = sorted(old_list, key = extract_number)
