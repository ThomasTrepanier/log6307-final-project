def get_output(category, order, i=0):
         output = {}
         for key in order[i:i+1]:
             for value in category[key]:
                 output[value] = get_output(category, order, i+1)
         if output == {}:
            return 0
         return output
