def get_last_line(file, how_many_last_lines = 1):

    # open your file using with: safety first, kids!
    with open(file, 'r') as file:

        # find the position of the end of the file: end of the file stream
        end_of_file = file.seek(0,2)
        
        # set your stream at the end: seek the final position of the file
        file.seek(end_of_file)             
        
        # trace back each character of your file in a loop
        n = 0
        for num in range(end_of_file+1):            
            file.seek(end_of_file - num)    
           
            # save the last characters of your file as a string: last_line
            last_line = file.read()
           
            # count how many '\n' you have in your string: 
            # if you have 1, you are in the last line; if you have 2, you have the two last lines
            if last_line.count('\n') == how_many_last_lines: 
                return last_line
get_last_line('lala.csv', 2)
