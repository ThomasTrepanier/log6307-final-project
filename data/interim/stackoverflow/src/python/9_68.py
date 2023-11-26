import pprint


def main():
    pp = pprint.PrettyPrinter(indent=2)
    path = "table.txt"
    res = {}
    with open(path, "r") as f:
        catagories = f.readline().strip().split(" | ")[-3:]
        for line in f:
            key_part, *values = line.strip().split(" | ")
            key = key_part.split()[-1]
            res[key] = {
                catagories[i]: values[i]
                for i in range(len(catagories))
            }
    pp.pprint(res)


if __name__ == "__main__":
    main()
