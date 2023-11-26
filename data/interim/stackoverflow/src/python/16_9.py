def __get_trimmed_quantity(self, quantity):
    trimmed_quantity = round(quantity / self.step_size) * self.step_size
    return trimmed_quantity

def __get_trimmed_price(self, price):
    trimmed_price = round(price / self.tick_size) * self.tick_size
    return trimmed_price
