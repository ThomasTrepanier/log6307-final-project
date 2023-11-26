def get_value(range):
    if range < 5:
        return 'Below 5'
    elif range < 10:
        return 'Between 5 and 10'
    else:
        return 'Above 10'

df['value'] = df.apply(lambda col: get_value(col['range']), axis=1)
