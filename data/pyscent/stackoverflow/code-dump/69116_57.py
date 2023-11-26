def split(df, based_on='subject_id', cv=5):
    splits = []
    based_on_uniq = df[based_on]#set(df[based_on].tolist())
    based_on_uniq = np.array_split(based_on_uniq, cv)
    for fold in based_on_uniq:
        splits.append(df[df[based_on] == fold.tolist()[0]])
    return splits


if __name__ == '__main__':
    df = pd.DataFrame([{'note_id': 1, 'subject_id': 1, 'category': 'test1', 'note': 'test1'},
                       {'note_id': 2, 'subject_id': 1, 'category': 'test2', 'note': 'test2'},
                       {'note_id': 3, 'subject_id': 2, 'category': 'test3', 'note': 'test3'},
                       {'note_id': 4, 'subject_id': 2, 'category': 'test4', 'note': 'test4'},
                       {'note_id': 5, 'subject_id': 3, 'category': 'test5', 'note': 'test5'},
                       {'note_id': 6, 'subject_id': 3, 'category': 'test6', 'note': 'test6'},
                       {'note_id': 7, 'subject_id': 4, 'category': 'test7', 'note': 'test7'},
                       {'note_id': 8, 'subject_id': 4, 'category': 'test8', 'note': 'test8'},
                       {'note_id': 9, 'subject_id': 5, 'category': 'test9', 'note': 'test9'},
                       {'note_id': 10, 'subject_id': 5, 'category': 'test10', 'note': 'test10'},
                       ])
    print(split(df))
