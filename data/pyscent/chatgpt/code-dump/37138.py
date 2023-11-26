import pandas as pd

def torchtext_dataset_to_df(dataset):
    data = []
    for example in dataset:
        data.append(vars(example))
    return pd.DataFrame(data)

# Convert to dataframe
df = torchtext_dataset_to_df(your_torchtext_dataset)
