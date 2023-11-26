from dataclasses import dataclass
from typing import List

@dataclass
class Window:
  index: int
  backward: List[int]
  forward: List[int]

def window(iterable, window_size, index):
  backward = iterable[max(0, index - window_size):index]
  forward = iterable[index + 1:index + 1 + window_size]
  return Window(index, backward, forward)
