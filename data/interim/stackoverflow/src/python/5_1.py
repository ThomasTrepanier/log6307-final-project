def ranges_overlap(a: range, b: range) -> bool:
    if b.start <= a.start < b.stop:
        return (a.start - b.start) % b.step == 0
    if a.start <= b.start < a.stop:
        return (b.start - a.start) % a.step == 0
    return False
