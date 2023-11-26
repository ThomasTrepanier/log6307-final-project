def main():
    total = 0
    while True:
        total += int(input("Insert one coin at a time: ").strip())
        coke = 50
        print(total)
        if total > coke:
            print("Change Owed =", total - coke)
            return
        elif total == coke:
            print("No Change Owed, Here's a coke ")
            return
        else:
            print("Amount Due =", coke-total)


main()
