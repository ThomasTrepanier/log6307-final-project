def convert(input_number, from_sys, to_sys):
    if from_sys == to_sys:
        return input_number
    func = converter_funcs[(from_sys, to_sys)]
    return func(input_number)
