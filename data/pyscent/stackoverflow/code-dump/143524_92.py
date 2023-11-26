def func1(doc):
    for c in symbols:
        doc = doc.replace(c, "")
    return doc


def func2(doc):
    return doc.translate(translate_table)


def func3(doc):
    return re.sub(regular_expression, "", doc)


def func4(doc):
    return "".join(c for c in doc if c not in symbols)
