from collections import defaultdict

lst = [("hello", "Blue"), ("hi", "Red"), ("hey", "Blue"), ("yo", "Green")]

colours = defaultdict(list)
for word, colour in lst:
    colours[colour].append((word, colour))

print(colours)
# defaultdict(<class 'list'>, {'Blue': [('hello', 'Blue'), ('hey', 'Blue')], 'Red': [('hi', 'Red')], 'Green': [('yo', 'Green')]})
