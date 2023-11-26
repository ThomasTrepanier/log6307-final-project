test_str = "6539923335"

def NumberStream(input_str):
    consec_count = 1
    for j, number in enumerate(input_str):
        if j == 0:
            continue
        if number == input_str[j-1]:
            consec_count += 1
        else:
            consec_count = 1
        if str(consec_count) == number:
            print ("Found consecutive numbers:", number)
            return "True"
    return

NumberStream(test_str)
