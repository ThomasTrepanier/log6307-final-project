def blackjack(numbers):
    if len(numbers) == 3 and max(numbers) <= 11 and min(numbers)>=1:
        sum_n = sum(numbers)
        res =[]
        if (sum_n  <= 21):
            res = sum_n 
        else:
            if 11 in numbers:
                res =sum_n-10
            else:
                res = "BUST"
        return res
    else:
        return "numbers length should be 3 and max is 11 and min 1"
