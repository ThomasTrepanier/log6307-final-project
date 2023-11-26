import pandas as pd
import numpy as np

# Example dataframe full of strings
df = pd.DataFrame.from_dict({'name':['Lebron James','Kevin Durant'],'points':['38','   '],'steals':['2.5',''],'position':['Every Position','SG'],'turnovers':['0','7']})   

def convertTypes(df):
    for col in df: 
        is_an_int = True
        is_a_float = True
        if(df[col].dtype == np.float64 or df[col].dtype == np.int64):
            # If the column's type is already a float or int, skip it
            pass
        else:
            # Iterate through each value in the column
            for value in df[col].iteritems():
                if value[1].isspace() == True or value[1] == '':
                    continue
                # If the string's isnumeric method returns false, it's not an int
                if value[1].isnumeric() == False: 
                    is_an_int = False
                # if the string is made up of two numerics split by a '.', it's a float
                if isinstance(value[1],str): 
                    if len(value[1].split('.')) == 2: 
                        if value[1].split('.')[0].isnumeric() and value[1].split('.')[1].isnumeric(): 
                            is_a_float = True 
                        else: 
                            is_a_float = False 
                    else: 
                        is_a_float = False 
                else: 
                    is_a_float = False 
            if is_a_float == True:
                # If every value's a float, convert the whole column
                # Replace blanks and whitespaces with np.nan
                df[col] = df[col].replace(r'^\s*$', np.nan, regex=True).astype(float)
            elif is_an_int == True:
                # If every value's an int, convert the whole column
                # Replace blanks and whitespaces with 0
                df[col] = df[col].replace(r'^\s*$', 0, regex=True).astype(int)

convertTypes(df)
