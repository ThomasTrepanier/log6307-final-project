def is_palindrome(s):
    odd_counter = 0
    for letter in s:
        if s.count(letter) % 2 != 0:
            odd_counter += 1

    if odd_counter > 1:
        return False
    return True
