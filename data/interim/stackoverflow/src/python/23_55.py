def lemma_conversion(sent):
    carrier_str = str()
    for token in sent:
        carrier_str = carrier_str + token.lemma_ + ' '
    return (carrier_str)
