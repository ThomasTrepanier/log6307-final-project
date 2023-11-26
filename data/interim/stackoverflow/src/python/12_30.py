def is_palindrome(input_string):
    new_string = input_string.lower()
    no_space = new_string.replace(" ","")

    reverse_string =new_string.replace(" ","")[::-1]
    if reverse_string==no_space:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
