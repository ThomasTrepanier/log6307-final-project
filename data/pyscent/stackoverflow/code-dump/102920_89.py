@dataclass
class Specs4:
    a: str
    b: str
    c: str

def create_spec(
        a: str,
        b: str = None,
        c: str = None,
):
    if b is None:
        b = 'Bravo'
    if c is None:
        c = 'Charlie'

    return Spec4(a=a, b=b, c=c)
