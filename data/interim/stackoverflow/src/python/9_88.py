def avg(nums):
    nums = list(nums)
    return round(sum(nums) / len(nums), 1)

d = {'actor1': {'salary': {'year1': 60, 'year2': 65}, 'age': 30},
     'actor2': {'salary': {'year1': 20, 'year2': 30}, 'age': 17},
     'actor3': {'salary': {'year1': 50, 'year2': 80}, 'age': 25}}

average = {'salary': {}}
average['age'] = avg(actor['age'] for actor in d.values())
for year in list(d.values())[0]['salary']:
    average['salary'][year] = avg(actor['salary'][year] for actor in d.values())

b = {'average': average}
