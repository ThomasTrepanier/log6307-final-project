class dfc:
  def __init__(self, df):
    self.df = df
    
  def func(self, num):
    self.df = self.df.selectExpr(f"id * {num} AS id")
  
  def func1(self, num1):
    self.df = self.df.selectExpr(f"id * {num1} AS id")
    
  def dfdis(self):
    self.df.show()
