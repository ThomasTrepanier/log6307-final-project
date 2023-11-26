lst = [('kol_id', '101152'), ('jnj_id', '7124166'), ('thrc_nm', 'VIR')]
def get_values(l):
    for idx, item in enumerate(l, start=1):
        yield f"input_v{idx} = {item}"
    
for _input in get_values(lst):
    print(_input)
