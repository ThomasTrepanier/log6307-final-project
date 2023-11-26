import string
correct = {char for char in string.ascii_letters + string.digits}
def is_correct(text):
    return {char for char in text}.issubset(correct)
print(is_correct('letters123')) # True
print(is_correct('???')) # False
print(is_correct('\n')) # False
