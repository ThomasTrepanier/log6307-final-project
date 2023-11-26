import string
import itertools


class BitMask(object):
    STR_TOKENS = string.ascii_letters
    STR_EMPTY = '_'
    STR_FULL = False

    def __init__(
            self,
            value=None,
            ignore=True):
        if isinstance(value, str):
            self.value = self.from_tokens(value, self.STR_TOKENS, ignore)
        else:
            self.value = value

    def __repr__(self):
        return bin(self.value)

    def __iter__(self):
        value = self.value
        while value:
            yield value & 1
            value >>= 1

    def to_tokens(self, tokens, empty, full):
        if full:
            return [
                token if value else empty
                for token, value in
                itertools.zip_longest(tokens, self, fillvalue=False)]
        else:
            return [
                token for token, value in zip(tokens, self) if value]

    def __str__(self):
        return ''.join(
            self.to_tokens(self.STR_TOKENS, self.STR_EMPTY, self.STR_FULL))

    def from_tokens(self, seq, tokens, ignore):
        if tokens is None:
            tokens = self.STR_TOKENS
        valid_tokens = set(tokens)
        value = 0
        for i, item in enumerate(seq):
            if item in valid_tokens:
                value |= 1 << tokens.index(item)
            elif not ignore:
                raise ValueError(f'Invalid input `{item}` at index: {i}.')
        return value

    def __add__(self, other):
        self.value |= other.value
        return self

    def __mul__(self, other):
        self.value &= other.value
        return self

    def __eq__(self, other):
        return type(self) == type(other) and self.value == other.value
