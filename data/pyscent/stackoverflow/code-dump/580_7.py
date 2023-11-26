##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Function to check all elements in a df column is same
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def check_all_are_equal_in_a_column_df(data_frame, column_name):
    data_list = data_frame[column_name].unique()
    data_set = set(data_list)
    if((len(data_set)) == 1):
        return_data = 1
    else:
        return_data = 0
    return return_data
