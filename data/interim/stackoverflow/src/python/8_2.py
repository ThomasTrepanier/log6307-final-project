def word_counter(passlist):
    do_count = lambda x: len(x.split())
    result=[]

    for elem in passlist:
        if isinstance(elem, list):
            result += [word_counter(elem)]
        elif isinstance(elem, str):
            result += [do_count(elem)]

    return result

print(word_counter([['We test robots'], ['Give us a try'], [' ']]))
# output: [[3], [4], [0]]

print(word_counter(['First of all', ['One more test'], [['Trying different list levels'], [' ']], 'Something more here']))
# output: [3, [3], [[4], [0]], 3]
