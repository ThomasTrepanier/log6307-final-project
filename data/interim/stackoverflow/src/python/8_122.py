def alternative_strings(strings):
        for i,x in enumerate(strings):
            if i % 2 == 0:
                print(x.upper(), end="")
            else:
                print(x.lower(), end= "")
        return ''


print(alternative_strings("Testing String"))
