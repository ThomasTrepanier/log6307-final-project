def deleteSearchTerm(inputFile):
#(1) Open the file

    df = pd.read_csv(inputFile)
    print(df)

#(2) Filter every row where the first letter is 's' from search term
    df = df[~pd.to_numeric(df['ProductOMS'],errors='coerce').isnull()]

    print(df)
    return df
