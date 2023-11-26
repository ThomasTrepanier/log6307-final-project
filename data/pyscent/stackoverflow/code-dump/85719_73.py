def romanToInt(s: str) -> int:
        # Define integer value to each roman 
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        # A list of integer values
        value = list(map(rom_val.get, s))

        # List to keep the checked roman
        checked = []
        for i, j in enumerate(value):
            if i == len(value) - 1:
                checked.append(j)
            elif j >= value[i+1]:
                checked.append(j)
            elif j < value[i+1]:
                checked.append(value[i+1] - j)

        print(checked)
        return sum(checked)

print(romanToInt("LVIII"))
