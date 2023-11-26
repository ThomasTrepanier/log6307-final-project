from dataclasses import dataclass, field

SHARED_LIST = ["your_values"]
    
@dataclass
class SomeClass:
    """
    """
    
    some_list: list = field(default_factory=lambda: SHARED_LIST)
