from dataclasses import dataclass
from functools import cached_property

@dataclass(frozen=True)
class Register:
    subsection: str
    name: str
    abbreviation: str
    address: int
    n_bits: int
    _get_method: Callable[[int], int]
    _set_method: Callable[[int, int], None]
    _save_method: Callable[[int, int], None]

    @cached_property
    def bit_mask(self) -> int:
        # The cache is used to avoid recalculating since this is a static value
        # (hence max_size = 1)
        return create_bitmask(
            n_bits=self.n_bits,
            start_bit=0,
            size=self.n_bits,
            set_val=True
            )

    def get(self) -> int:
        raw_value = self._get_method(self.address)
        return raw_value & self.bit_mask

    def set(self, value: int) -> None:
        self._set_method(
            self.address,
            value & self.bit_mask
            )

    def save(self, value: int) -> None:
        self._save_method(
            self.address,
            value & self.bit_mask
            )
