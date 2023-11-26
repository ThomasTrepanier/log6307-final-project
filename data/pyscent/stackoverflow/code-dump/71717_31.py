class NicelyPrintingDict():
    def __init__(self, some_dictionary):
        self.some_dictionary = some_dictionary

    def __str__(self):
        s = ''
        for key, value in self.some_dictionary.items():
            s += key + ': ' + str(value) + ' ' 
        return s.strip()
