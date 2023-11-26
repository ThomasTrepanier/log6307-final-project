import random


class Lbom():
  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      if key == 'color':
        self.print_color(value) 
      if key == 'combo':
        self.combo(value)


  def combo(self, combination):
    print(combination * random.randint(0,100))


  def print_color(self, color):
    print('color: {}'.format(color))
