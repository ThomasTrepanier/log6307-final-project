def chars_and_nums_efficient(text):
    if not text:
        return [], []
    digits, chars = [], []
    for c in text:
        if c.isdigit():
            digits.append(c)
        elif c.isalpha():
            chars.append(c)
    return digits, chars
