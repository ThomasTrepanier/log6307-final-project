def remove_duplicate_dataframes(dfs: list) -> list:
    if len(dfs) < 2:
        return dfs

    unique_dfs = []
    for idx, df in enumerate(dfs):
        if len(unique_dfs) == 0:
            unique_dfs.append(df)
            continue

        dfs_copy = deepcopy(dfs)
        dfs_copy.pop(idx)
        if any([df_.equals(df) for df_ in dfs_copy]):
            continue
        else:
            unique_dfs.append(df)

    return unique_dfs
