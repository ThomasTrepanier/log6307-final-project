My_List = ["adopt", "bake", "beam"]

def ed(word): return word+"d" if word[-1]=="e" else word+"ed"

Past_Tense = list(map(ed, My_List)) # ['adopted', 'baked', 'beamed']
