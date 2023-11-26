def tokenize(str):
    idx = [x for x, v in enumerate(str) if v == '\"']
    if len(idx) % 2 != 0:
        idx = idx[:-1]
    memory = {}
    for i in range(0, len(idx), 2):
        val = str[idx[i]:idx[i+1]+1]
        key = "_"*(len(val)-1)+"{0}".format(i)
        memory[key] = val
        str = str.replace(memory[key], key, 1)        
    return [memory.get(token, token) for token in str.split(",")]  
