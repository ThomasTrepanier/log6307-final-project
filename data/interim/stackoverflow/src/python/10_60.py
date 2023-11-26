import json
import sys
import os.path

def main(argv):

    #Load JSON
    current_folder = os.path.dirname(os.path.realpath(__file__))
    with open(current_folder + '\\input.json') as json_file:  
        data = json.load(json_file)

    #Flatten (using for loops)
    flat=[]
    for entry in data['row']:
        for column in entry['column']:
            flat.append(column['text'])

    # OR, Flatten the pythonic way (using list comprehension)
    # looks strange at first but notice
    #   1. we start with the item we want to keep in the list
    #   2. the loops order is the same, we just write them inline 
    flat2 = [ column['text'] for entry in data['row'] for column in entry['column'] ]


    #Format data for saving to JSON
    output = {}
    output['@index']=data['@index']
    output['row'] = flat #or flat2 

    #Save to JSON
    with open('flat.txt', 'w') as outfile:
        json.dump(output, outfile, indent=4)

if __name__ == "__main__":
   main(sys.argv[1:])
