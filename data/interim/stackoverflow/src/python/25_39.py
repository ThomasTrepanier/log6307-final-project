def main():
    print("Enter two numbers and I will tell you the sum of the numbers.")
    print("Press 'q' at anytime to exit.")
    val = []
    while True:

        check_value = lambda x: 'quit' if x.lower() == 'q' or x.lower() == 'quit' else int(x)
        if not val:
            value = input("First number: ")
        elif len(val) == 2:
            answer = sum(val)
            print(f"\nThe answer is: {answer}")
            print('==='*15 + ' < ' + f'PROGRAM RESTARTING' + ' > ' + '==='*15)

            val[:] = []
            continue
        else:
            value = input("Second number: ")


        try:
            check_ = check_value(value)
            val.append(check_)
        except ValueError:
            print("Please enter a number!")
            continue
        finally:
            if check_ == 'quit':
                print('Program is stopping....')
                break
            else:
                pass


if __name__ == '__main__':
    main()
