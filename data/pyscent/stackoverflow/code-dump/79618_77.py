import re

def split_and_lower(s): 
    return list(map(str.lower, re.split(s, '[^\w]*'))) 

L = ["Hello, My Name is John", "Good Afternoon, my name is David", "I am three years old"] 
result = list(map(split_and_lower, L))
print(result)
