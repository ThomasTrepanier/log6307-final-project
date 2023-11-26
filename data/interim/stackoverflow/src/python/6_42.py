from pathlib import Path

def delete_search_term(input_file, column):
    """
    Takes in a file and removes any strings from a given column
    input_file : path to your file.
    column : column with strings that you want to remove.

    """
    file_path = Path(input_file)

    if not file_path.is_file():
        raise Exception('This file path is not valid')

    df = pd.read_csv(input_file)

    #(2) Filter every row where the first letter is 's' from search term
    df = df[~pd.to_numeric(df[column],errors='coerce').isnull()]
    print(f"Creating file as:\n{file_path.parent.joinpath(f'{file_path.stem}_edited.csv')}")
    return df.to_csv(file_path.parent.joinpath(f"{file_path.stem}_edited.csv"),index=False)
