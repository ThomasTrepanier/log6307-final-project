def flatten(el):
    flattened = [flatten(children) for children in el.children()]
    res = [el]
    for c in flattened:
        res += c
    return res

cnn = nn.Sequential(Custom_block_1, Custom_block_2)
layers = flatten(cnn)
