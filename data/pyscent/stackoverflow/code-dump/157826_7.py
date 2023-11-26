class Wildcard:
    def __eq__(self, anything):
        return True

a = [['1','2','3','a','b'],
     ['4','5','6','c','d'],
     ['7','8','9','e','f']]

wc = Wildcard()

print(a.index(['4', '5', '6', wc, wc]))
