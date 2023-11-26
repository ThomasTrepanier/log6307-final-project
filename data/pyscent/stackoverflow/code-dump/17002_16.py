import numpy as np

class MyClass(object):
    def __init__(self):
        #you'll have to set the numerical values to something that causes num_var_list to not loop infinitely
        self.number_list = None
        self.number_exit = 0
        self.number_target = 0
        self.price_buy = 0

    # This function generates a list of numbers under certain rules
    def num_var_list(self):
        self.number_list = []
        self.number_target = self.number_exit
        num_max_robot = (self.number_target * 20) / 100
        while num_max_robot > 0:
            num_robot = np.random.randint(1,int(num_max_robot))
            if num_robot > self.number_target:
                    self.number_list.append(self.number_target)
            else: 
                self.number_list.append(num_robot)
            self.number_target = self.number_target - self.number_target
        return self.number_list
            
    # This function generates a random number between a certain range
    def fun_price_buy(self):
        self.price_buy = np.random.randint(50000,300000)
        return self.price_buy

    # This function generates a random number between a certain range
    def fun_mx_buy(self):
        self.number_exit = np.random.randint(50, 150)
        return self.number_exit

def main():
    lista_number_list = []
    lista_price_buy = []
    lista_mx_buy = []
    
    my_class_instance = MyClass()

    # This loop append each function 50 times to a new list
    while len(lista_price_buy) <= 50: 
        lista_number_list.append(my_class_instance.num_var_list())
        lista_price_buy.append(my_class_instance.fun_price_buy())
        lista_mx_buy.append(my_class_instance.fun_mx_buy())

if __name__ == '__main__':
    main()
