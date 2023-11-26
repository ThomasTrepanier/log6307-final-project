def sortNumbers(text):
    # replace all non-digit characters by space, split result
    numbers = ''.join(t if t.isdigit() else ' ' for t in text).split()

    # order descending by integer value
    numbers.sort(key=lambda x:-int(x))  

    # replace all found numbers - do not mess with the original string with 
    # respect to splitting, spaces or anything else - multiple spaces
    # might get reduced to 1 space if you "split()" it.
    for n in numbers:
        text = text.replace(n, "{}")

    return text.format(*numbers)  # put the sorted numbers back into the string

for text in ["I am 5 years and 11 months old",
            "I am 28 years 9 months 11 weeks and 55 days old",
            "What is 5 less then 45?",
            "At 49th Street it is 500.", "It is $23 and 45."]:

    print(sortNumbers(text))
