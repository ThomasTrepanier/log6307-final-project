def foo(bar: Sequence[int] = []) -> list[int]:
    if isinstance(bar, list):
        # reveal_type(bar)  # => Revealed type is "builtins.list[Any]"
        bar.append(0)
    return sorted(bar)
