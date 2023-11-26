from dataclasses import dataclass
import inspect

@dataclass
class Config:
    var_1: str
    var_2: str

    @classmethod
    def from_dict(cls, env):      
        return cls(**{
            k: v for k, v in env.items() 
            if k in inspect.signature(cls).parameters
        })


# usage:
params = {'var_1': 'a', 'var_2': 'b', 'var_3': 'c'}
c = Config.from_dict(params)   # works without raising a TypeError 
print(c)
# prints: Config(var_1='a', var_2='b')
