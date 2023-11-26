from typing import Any
from types import SimpleNamespace as SNS


class RecursiveNS(SNS):
    def __init__(self, **kwargs):
        self.__dict__.update(self.parse(kwargs).__dict__)

    @staticmethod
    def parse(d: dict[str, Any]) -> SNS:
        """Static method that takes dictionary as an argument,
        and returns """
        x = SNS()
        for k, v in d.items():
            setattr(
                x,
                k,
                RecursiveNS.parse(v)
                if isinstance(v, dict)
                else [RecursiveNS.parse(e) for e in v]
                if isinstance(v, list)
                else v,
            )
        return x
