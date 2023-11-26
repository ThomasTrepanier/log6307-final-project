def findvalue(df, value):
    # check the words which contain the value
    inlist = [value in word for word in df['identifierOne']]

    one = []
    two = []

    # now we explicitly check all of the booleans in `inlist`
    for i, boolean in enumerate(inlist):
        if boolean:
            one.append(df['identifierOne'][i])
            two.append(df['identifierTwo'][i])

    # only write to `output` if there is something to write
    if one:
        output.loc[df.name, 'identifierOne'] = one
        output.loc[df.name, 'identifierTwo'] = two
