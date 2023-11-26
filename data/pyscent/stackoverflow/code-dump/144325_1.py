class Account:

    number_of_accounts = 0  # class attribute, not initialised for every instance

    def __init__(self):
        # whatever init code
        Account.number_of_accounts += 1

account_1 = Account()
account_2 = Account()
account_3 = Account()

print(Account.number_of_accounts)
