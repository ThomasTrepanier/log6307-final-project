a = 3 # This is globally defined

def foo(a):
  a = 3 * a
  return a

print(foo(a))
9
