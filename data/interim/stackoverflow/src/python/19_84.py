test_str = "6539923335"

def NumberStream(input_str):
    for i in range(10):
        consec_num = str(i)*i
        if consec_num in input_str:
            print("Found", consec_num)
            return "True"
    return "False"

print(NumberStream(test_str))
