def func(rowws = df.iterrows(), N=3):
    selected = []
    for i in range(N):
        selected.append(next(rowws))

    yield selected

selected = next(func())
