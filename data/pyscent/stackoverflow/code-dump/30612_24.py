def rearrange_name(name):
    tokens = name.split(", ")
    return " ".join(reversed(tokens))

name=rearrange_name("Kennedy, John F.")
print(name)
