def split_text(text):
    middle = len(text)//2
    under = text.rfind(" ", 0, middle)
    over = text.find(" ", middle)
    if over > under and under != -1:
        return (text[:,middle - under], text[middle - under,:])
    else:
        if over is -1:
              raise ValueError("No separator found in text '{}'".format(text))
        return (text[:,middle + over], text[middle + over,:])
