def main():
    # np.load('File.csv')
    raise ValueError
    print("In main")

def main1():
    # np.load('File1.csv')
    raise ValueError
    print("In main1")

def main2():
    # np.load('File2.csv')
    raise ValueError
    print("In main2")

for i in range(1, 10):
    try:
        main()
        main2()
        main3()
    except Exception as e:
        print(e)
    else:
        break
