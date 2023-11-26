def foo(input_message):

    c = 0 
    output_message = ""

    for m in input_message:
        if (c%2==0):
            output_message = output_message + m.lower() 
        else: 
            output_message = output_message + m.upper()
        c = c + 1 

    return output_message
