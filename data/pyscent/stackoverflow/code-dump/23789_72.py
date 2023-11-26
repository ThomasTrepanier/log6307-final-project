def rng_list():
    while True:
        rng_list = []
        current_sum = 0
        for i in range(14):
            r = random.randint(5, 20)
            rng_list.append(r)
            current_sum+= r
            if not 5*(14-i) <= 227-current_sum <= 20*(14-i): #`i` goes from 0 to 14, so 14-i is how many (from 15) numbers are still not calculated
                break
        if len(rng_list) == 14:
            rng_list.append(227-current_sum)
            return rng_list
        print("Pass failed with list {}, sum {} - trying again.".format(rng_list, current_sum)) #added to debug/show how it works
