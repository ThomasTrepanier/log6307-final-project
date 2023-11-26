def two_string(a: str, b: str) -> dict:
    return {idx: match[0] for idx, match in enumerate(zip(a.lower(),b.lower())) if match[0] == match[1]}

two_string('The Holy Grail', 'Life of Brian')

# {5: 'o', 11: 'a'}
