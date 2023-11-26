@dataclass
class Specs3(NoneRefersDefault):
    a: str
    b: str = DefaultVal('Bravo')
    c: str = DefaultVal('Charlie')

r3 = Specs3('Apple', None, 'Cherry')  # Specs3(a='Apple', b='Bravo', c='Cherry')
