myList = [4, 1, 88, 44, 3,-1,-7,-19,-0.5,-0.2]

def compute_closest_to_zero(myList):
    positive = []
    negative = []
    if len(myList) == 0:
        print('0')
    else:
        for i in myList:
            if i >= 0:
                positive.append(i)
                #print(positive)
            else:
                negative.append(i)
                #print(negative)
                #print(min(positive))

                
    if min(positive) + max(negative) < 0:
        print(min(positive))
    else:
        print(max(negative))
    return

Blockquote

compute_closest_to_zero(myList)
