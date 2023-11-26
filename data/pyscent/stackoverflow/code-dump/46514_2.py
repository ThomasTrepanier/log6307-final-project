from dataclasses import dataclass, asdict

@dataclass
class Human:
    name: str
    age: int = None
    height: float = None
    gender: str = None
    programmer: bool = False

jason = Human(name="jason", programmer=True)

jason_details = asdict(jason)
print(jason_details)
