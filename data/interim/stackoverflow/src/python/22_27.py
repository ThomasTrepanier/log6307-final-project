coke_price = 50
payment = coke_price


def main():
    global coke_price
    global payment

    while True:
        money_input = int(input("Enter one coin at a time: ").strip())
        payment = payment - money_input

        if payment < 0:
            print("Change Owed =", -payment)
            return
        elif payment == 0:
            print("No Change Owed, Here's a coke ", payment)
            return
        else:
            print("Amount Due =", payment)

main()
