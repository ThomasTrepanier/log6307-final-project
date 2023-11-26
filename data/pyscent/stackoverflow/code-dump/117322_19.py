MISSING = object()
def dataclassWith(other, clz=None, **kw):
    if clz is None: clz = other.__class__

    k = other.__dict__.copy()
    k.update(kw)
    return clz(**{k:v for k,v in k.items()
                  if getattr(clz, k, MISSING) is not MISSING})


class TestDataclassUtil(unittest.TestCase):
    def test_dataclassWith(self):
        @dataclasses.dataclass
        class X():
            x:int = 1
            z:int = 99

        @dataclasses.dataclass
        class Y(X):
            y:int = 2

        r = dataclassWith(Y(x=2), y=3)
        self.assertTrue(isinstance(r, Y))
        self.assertTrue(r.x==2)
        self.assertTrue(r.y==3)
        self.assertTrue(r.z==99)

        r = dataclassWith(Y(x=2), X, z=100)
        self.assertTrue(isinstance(r, X))
        self.assertTrue(r.x==2)
        self.assertTrue(r.z==100)
