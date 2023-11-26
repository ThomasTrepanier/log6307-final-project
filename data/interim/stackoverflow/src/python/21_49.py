def foo(x,y1=None,y=None):
  if y1 is not None:
    print('y was passed positionally!')
  else:
    print('y was passed with its keyword')
