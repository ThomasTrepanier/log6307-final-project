def rng_list(): 
    while True: 
        rng_list = [random.randint(5, 20) for _ in range(14)] 
        if 207 <= sum(rng_list) <= 222: 
            break 
    rng_list.append(227 - sum(rng_list))
    return rng_list
