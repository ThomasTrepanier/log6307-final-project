def dup_char_remover(input):
    output=""
    t=""
    for c in input:
        if t!=c:
            output = output + c
        t=c
    return output

input = "hiiii how arrrre youuu"
output=dup_char_remover(input)
print(output)
