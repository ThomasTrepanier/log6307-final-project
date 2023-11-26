import math
from typing import Callable, Optional, TypeVar

# Define the type variables
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

# A Partial function is a function that may not provide an answer
PartialFunction = Callable[[A], Optional[B]]

# Identity morphism
def identity(a: A) -> Optional[A]:
    return a

# Composition of morphisms
def compose(m1: PartialFunction[A, B], m2: PartialFunction[B, C]) -> PartialFunction[A, C]:
    def composed(a: A) -> Optional[C]:
        tmp = m1(a)
        if tmp is None:
            return None
        else:
            return m2(tmp)
    return composed

# Safe square root function
def safe_square_root(x: float) -> Optional[float]:
    return math.sqrt(x) if x >= 0 else None

# Safe reciprocal function
def safe_reciprocal(x: float) -> Optional[float]:
    return 1 / x if x != 0 else None

# Compose safe_square_root and safe_reciprocal
# This function will first take the reciprocal of a number, and then take the square root of the result
composed_function = compose(safe_reciprocal, safe_square_root)

# Now we can test our composed function

def test():
    # Test with some values
    print(composed_function(4))  # Should print 0.5
    print(composed_function(-4))  # Should print None because sqrt is not defined for negative numbers
    print(composed_function(0))  # Should print None because reciprocal is not defined for 0

test()
