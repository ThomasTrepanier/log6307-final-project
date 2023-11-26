import collections
import itertools
import string


def main():
    words = ["tree", "bone", "indigo", "developer"]
    no_repeated_letters = (set(word) for word in words)
    letter_stream = itertools.chain.from_iterable(no_repeated_letters)
    counter = collections.Counter(letter_stream)
    # set zeros for unseen letters, to match poster's answer.
    for letter in string.ascii_lowercase:
        if letter not in counter:
            counter[letter] = 0
    # print result.
    for key in sorted(counter):
        print(key, counter[key])


if __name__ == '__main__':
    main()
