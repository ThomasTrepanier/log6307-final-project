import re
import pandas as pd

SEP_RE = re.compile(r":\s+")
DATA_RE = re.compile(r"(?P<term>[a-z]+)\s+(?P<weight>\d+\.\d+)", re.I)


def parse(filepath: str):
    def _parse(filepath):
        with open(filepath) as f:
            for line in f:
                id, rest = SEP_RE.split(line, maxsplit=1)
                for match in DATA_RE.finditer(rest):
                    yield [int(id), match["term"], float(match["weight"])]
    return list(_parse(filepath))
