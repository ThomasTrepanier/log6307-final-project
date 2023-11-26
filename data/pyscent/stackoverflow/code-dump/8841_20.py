import re
import pandas as pd 
from io import StringIO


def read_markdown_table(table_str: str) -> pd.DataFrame:
    """Read markdown table from string and return pandas DataFrame."""
    # Ref: https://stackoverflow.com/a/76184953/
    cleaned_table_str = re.sub(r'(?<=\|)( *[\S ]*? *)(?=\|)', lambda match: match.group(0).strip(), table_str)
    df = pd.read_table(StringIO(cleaned_table_str), sep="|", header=0, skipinitialspace=True) \
           .dropna(axis=1, how='all') \
           .iloc[1:]
    df.columns = df.columns.str.strip() 
    return df
