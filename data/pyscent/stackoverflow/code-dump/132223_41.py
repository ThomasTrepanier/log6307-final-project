def count_vowels(word):
    # all letters you are interested in 
    allowed = frozenset("aeiou")
    # get the len of the intersection between allowed and lower cased word
    return len(allowed.intersection( word.lower()))

tests = [("swEet",1), ("Aaa aeeE", 2),("eiOuayOI j_#Ra", 5)]

for t in tests:
    print(t[0], "is", count_vowels(t[0]), "should be", t[1])
