def is_even(stack):
        for i in range(0, len(stack), 2):
            temp = stack[i]
            stack[i] = stack[i+1]
            stack[i+1] = temp
        return stack

def is_odd(stack):
    for i in range(0, len(stack - 1), 2):
        temp = stack[i]
        stack[i] = stack[i+1]
        stack[i+1] = temp
    return stack

stack = []
word = input("Type Your word here: ")
wordChars = list(word)

for i in range(len(wordChars)):
    stack.append(wordChars[i])

print(stack)
if len(stack) % 2 == 0:
    new_stack = is_even(stack)
else:
    new_stack = is_odd(stack)
