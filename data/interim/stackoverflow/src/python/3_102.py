WORD_DICT = {"THEIR":"THEIR",
             "BUSINESS":"BISINESS",
             "WINDOWS":"WINDMILL",
             "WERE":"WEAR",
             "SAMPLE":"SAMPLE"}

def find_correct(word_dict):

    correct, almost_correct, incorrect = 0, 0, 0

    for key, value in WORD_DICT.items():

        diff_list = set(list(key)).symmetric_difference(set(list(value)))  
        diff = len(diff_list)

        if diff == 0:
            correct += 1
        elif diff <= 2:
            almost_correct += 1
        elif diff > 2:
            incorrect += 1


    print(correct, almost_correct, incorrect)


find_correct(WORD_DICT)
