def shunting_yard(expression):
    def higher_precedence(op1, op2):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedences[op1] > precedences[op2]

    output_queue = []
    operator_stack = []

    tokens = expression.split(' ')

    for token in tokens:
        if token.isnumeric():
            output_queue.append(int(token))
        elif token in '+-*/^':
            while operator_stack and operator_stack[-1] in '+-*/^' and higher_precedence(operator_stack[-1], token):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if type(token) is int:
            stack.append(token)
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+': stack.append(val1 + val2)
            elif token == '-': stack.append(val1 - val2)
            elif token == '*': stack.append(val1 * val2)
            elif token == '/': stack.append(val1 / val2)
            elif token == '^': stack.append(val1 ** val2)

    return stack[0]

# usage:
expression = '3 + 4 * 2 / ( 1 - 5 ) ^ 2'
postfix = shunting_yard(expression)
result = evaluate_postfix(postfix)
print(result)
