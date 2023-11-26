def get_max(int_list):
    best_max = False
    for value in int_list:
        if best_max == False or best_max < value:
            best_max = value
    return best_max


int_list = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print ( get_max(int_list) )
