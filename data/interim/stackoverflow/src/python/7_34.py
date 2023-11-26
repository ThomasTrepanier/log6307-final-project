range_of_ids = range(len(ids))

def score_calculation(s_id1,s_id2):
    s1 = set(list(df.loc[df['id'] == ids[s_id1]]['list_of_value'])[0])
    s2 = set(list(df.loc[df['id'] == ids[s_id2]]['list_of_value'])[0])
    # Resultant calculation s1&s2
    return round(len(s1&s2)/len(s1) , 2)


dic = {indexQFID:  [score_calculation(indexQFID,ind) for ind in range_of_ids] for indexQFID in range_of_ids}
dfSim = pd.DataFrame(dic)
print(dfSim)
