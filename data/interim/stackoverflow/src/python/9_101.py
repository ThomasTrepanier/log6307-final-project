def select_in_df(start, end):
    selected = data_frame[start:end]
    selected = select.values.tolist()
    return selected


print(select_in_df(0, 4)) #to update the start and end values, you can use any loop or whatever is your convenience 

#here is an example 
start = 0
end = 3
for i in range(10): #instead of range you can use data_frame.iterrows() 
    select_in_df(start, end+1) #0:4 which gives you 3 rows
    start = end+1
    end = i
