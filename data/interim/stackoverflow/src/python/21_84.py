def groups_per_user(group_dictionary):
    user_groups = {}
    for grp, users in group_dictionary.items():
        for user in users:
            if user in user_groups:
                user_groups[user].append(grp)
            else:
                user_groups[user] = [grp]

    return (user_groups)
