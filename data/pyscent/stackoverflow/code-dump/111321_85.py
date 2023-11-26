def groups_per_user(group_dictionary):
    user_groups = {}
    for group in group_dictionary:
        for user in group_dictionary[group]:
            if user not in user_groups:
                user_groups[user] = []
            if group not in user_groups[user]:
                user_groups[user].append(group)
    return user_groups

mylist = {"local": ["admin", "userA"],
          "public":  ["admin", "userB"],
          "administrator": ["admin"] }

print(groups_per_user(mylist))
# {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}

