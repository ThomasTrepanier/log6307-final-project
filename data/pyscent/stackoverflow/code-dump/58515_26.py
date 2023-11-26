def flatten(model):
    submodules = list(model.children())
    if len(submodules) == 0:
        return [model]
    else:
        res = []
        for module in submodules:
            res += flatten(module)
        return res
