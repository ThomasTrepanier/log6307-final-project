def expand_row(row):
    return pd.DataFrame({
        'name': row['name'], # row.name is the name of the series
        'id': row['id'],
        'app_name': [app[0] for app in row.apps],
        'app_version': [app[1] for app in row.apps]
    })

temp_dfs = df.apply(expand_row, axis=1).tolist()
expanded = pd.concat(temp_dfs)
expanded = expanded.reset_index() # put index in the correct order

print(expanded)

#     name  id app_name app_version
# 0   john   1     app1          v1
# 1   john   1     app2          v2
# 2   john   1     app3          v3
# 3  smith   2     app1          v1
# 4  smith   2     app4          v4
