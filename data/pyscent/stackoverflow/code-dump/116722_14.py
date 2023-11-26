#vending machine
def CountMoneyAndIssueDrink():
    
    total_coins = 0
    coke_price = 10
    change = 0
    
    while True:
        insertedcoins = int(input("Insert coins:"))
        total_coins += insertedcoins
        print(total_coins ," total coins inserted")
        
        if total_coins <= 0:
            print("Insert some coins")
            CountMoneyAndIssueDrink()
            return
        elif(total_coins > coke_price):
            change = total_coins - coke_price
            print("enjoy coke!!, here is the change:", change)
            break
        elif(total_coins == coke_price):
            print("enjoy coke!!")
            break


if __name__ == "__main__":
    CountMoneyAndIssueDrink()
