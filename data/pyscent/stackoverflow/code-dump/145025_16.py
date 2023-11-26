def main():
    b = [1, 3, 2, 5, 4, 7, 6]
    node = 5
    for i in range(-1, -len(b), -1):
        if b[i] == node:
            for j in b[i+1:]:
                print(j)
            return 0
    for i in b:
        print(i)


if __name__ == "__main__":
    main()
