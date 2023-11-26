words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse']
def get_results(_start, _current, _seen):
  if all(c in _seen for c in words if c[0] == _start[-1]):
    yield _current
  else:
      for i in words:
        if i[0] == _start[-1]:
          yield from get_results(i, _current+[i], _seen+[i])


new_d = [list(get_results(i, [i], []))[0] for i in words]
final_d = max([i for i in new_d if len(i) == len(set(i))], key=len)
