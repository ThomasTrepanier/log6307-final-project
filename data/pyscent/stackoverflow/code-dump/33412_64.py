def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    
    for word in input_string:
        if word != " ":
            new_string = new_string.strip().lower() + word
            reverse_string = word + reverse_string.strip().lower()
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
