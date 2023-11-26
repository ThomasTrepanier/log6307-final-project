def num_var_list():
    number_exit=fun_mx_buy()
    number_list = []
    number_target = number_exit
    num_max_robot = (number_target * 20) / 100
    while num_max_robot > 0:
        num_robot = np.random.randint(1, int(num_max_robot))
        if num_robot > number_target:
            number_list.append(number_target)
        else:
            number_list.append(num_robot)
        number_target = number_target - number_target
    return number_list
