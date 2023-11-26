def combine_jsons():
    file_list = ['first.json', 'second.json',... ,'last.json']
    all_data_dict = {}
    for json_file in file_list:
       with open(json_file,'r+') as file:
           # First we load existing data into a dict.
           file_data = json.load(file)
       all_data_dict.update(file_data)
    with open('merged_data.json', "w") as outfile:# save to json file
        json.dump(all_data_dict, outfile)
