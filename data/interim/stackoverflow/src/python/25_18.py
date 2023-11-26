def find_substring_length_k_most_vowels(s: str, k: int) -> str:
    '''Returns first substring of length k that has the max number of vowels.'''
    vowels = set('aeiou')
    max_vowel_count = curr_vowel_count = 0
    max_window_start, max_window_end = 0, -1
    window_start = 0
    for window_end, ch in enumerate(s):
        if ch in vowels:
            curr_vowel_count += 1
        if window_end - window_start + 1 == k:
            if curr_vowel_count > max_vowel_count:
                max_vowel_count = curr_vowel_count
                max_window_start, max_window_end = window_start, window_end
            curr_vowel_count -= 1 if s[window_start] in vowels else 0
            window_start += 1
    return s[max_window_start:max_window_end + 1]


def main() -> None:
    s = 'azerdii'
    k = 5
    print(find_substring_length_k_most_vowels(s, k))


if __name__ == '__main__':
    main()
