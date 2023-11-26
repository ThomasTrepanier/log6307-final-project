WORD_DICT = {"THEIR":"THEIR",
             "BUSINESS":"BISINESS",
             "WINDOWS":"WINDMILL",
             "WERE":"WEAR",
             "SAMPLE":"SAMPLE"}

second_dict = {'WHIZZY': 'MIZZLY', 'PRETTY': 'PRESEN'}

def find_correct(k, v):

    k, v = list(k), list(v)
    for k_letter in k:
        if k_letter in v:
            idx = v.index(k_letter)
            v.pop(idx)
    if len(v) == 0:
        return "correct"
    elif len(v) == 1:
        return "almost correct"
    else:
        return "incorrect"

def top_level_func(word_dict):

    d = {"correct":0, "almost correct":0, "incorrect":0}
    for k, v in word_dict.items():
        response = find_correct(k, v)
        d[response] += 1

    return d

results = top_level_func(second_dict)
for item in results.items():
    print("{} = {} instances".format(*item))
