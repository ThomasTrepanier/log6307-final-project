class Customer:
    def __init__(self, age, totalsales, paymenttype):
        self.age = age
        self.totalsales = totalsales
        self.paymenttype = paymenttype


c = Customer(21, 3000, 2)
if c.age > 18 or c.totalsales > 5000 or c.paymenttype == 1:
    print('Hello World!')
