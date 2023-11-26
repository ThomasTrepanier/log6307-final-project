def convert(list_dict, old_text, new_text):
    def replace_dict(old_dict, old_text, new_text):
        return {key.replace(old_text, new_text) : val.replace(old_text, new_text) for key, val in old_dict.items()}
        
    for i in range(len(list_dict)):
        list_dict[i] = replace_dict(list_dict[i], old_text, new_text)

orig= [{"health": "good", "status": "up", "date":"2022.03.10","device.id":"device01"}, {"health": "poor", "status": "down", "date":"2022.03.10","device.id":"device02"}]

convert(orig, '.', '-')
print(orig)
