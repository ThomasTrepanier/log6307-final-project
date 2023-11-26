def using_replace(text, symbols_to_replace, replacement=' '):
    for char in symbols_to_replace:
        text = text.replace(char, replacement)

    return text

def using_join(text, symbols_to_replace, replacement=' '):
    return ''.join(
        replacement if char in symbols_to_replace else char
        for char in text)

def using_translate(text, symbols_to_replace, replacement=' '):
    translation_dict = str.maketrans(
        dict.fromkeys(symbols_to_replace, replacement))

    return text.translate(translation_dict)
