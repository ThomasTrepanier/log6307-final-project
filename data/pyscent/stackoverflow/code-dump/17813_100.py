from collections import defaultdict

name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]

name_dict = defaultdict(list)

for first_name in set([name.split()[0] for name in name_list]):
    name_dict[first_name] = [name for name in name_list if name.split()[0] == first_name]

print(name_dict)
#defaultdict(<class 'list'>, {'Maren': ['Maren Fry'], 'David': ['David Joyner', 'David Zuber'], 'Nicol': ['Nicol Barthel'], 'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Odle', 'Shelba Fry'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber']})
