@dataclass
class Marker:
    a: float
    b: float = 1.0

marker_a = Marker(0.5)

marker_b = Marker(**marker_a.__dict__)

marker_b

# Marker(a=0.5, b=1.0)
