import os
from distutils.util import strtobool
from typing import Dict, Any

os.environ["SSL"] = "0"
os.environ["PORT"] = "99999"


def type_env() -> Dict[str, Any]:
    d: Dict[str, Any] = dict(os.environ)
    for key in d:
        try:
            d[key] = bool(strtobool(d[key]))
            continue
        except ValueError:
            pass
        try:
            d[key] = int(d[key])
            continue
        except ValueError:
            pass
        try:
            d[key] = float(d[key])
            continue
        except ValueError:
            pass
    return d


env = type_env()
print(type(env["SSL"]))
print(type(env["PORT"]))

if not env["SSL"]:  # <-- I'd like this to be cast to boolean and typed as a boolean
    print("Connecting w/o SSL!")
if 65535 < env["PORT"]:  # <-- I'd like this to be cast to int and typed as an int
    print("Invalid port!")
