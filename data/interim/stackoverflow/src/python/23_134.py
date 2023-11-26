def blackjack(a,b,c):

    Ace_count = [a,b,c].count(11)

    total = sum([a,b,c])

    if total <= 21:
        return ("Not busted", total)

    while total > 21:
        if Ace_count > 0:
            Ace_count -= 1
            total -= 10
        else:
            return "Bust"

    return ("Not busted", total)

print(blackjack(11,11,11))
