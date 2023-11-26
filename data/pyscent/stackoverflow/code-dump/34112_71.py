def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = input_string.replace(" ", "")
    new_string = new_string.lower()
    reverse_string = new_string[::-1]
    reverse_string = reverse_string.lower()
    # Traverse through each letter of the input string
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
