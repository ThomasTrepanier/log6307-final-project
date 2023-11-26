def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for key,value in group_dictionary.items():
        # Now go through the users in the group
        for letter in value:
            if letter in user_groups:
                user_groups[letter] += [key]             
            else :
                user_groups[letter] = [key]
            
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
    "public":  ["admin", "userB"],
    "administrator": ["admin"] }))
