from dis import dis


def list_constructor():
    return list()

def list_literal():
    return []


print("constructor:")
dis(list_constructor)

print()

print("literal:")
dis(list_literal)
