def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group in group_dictionary:
        # Now go through the users in the group
        for user in group_dictionary[group]:
            try:
                user_groups[user].append(group)
            except KeyError:
                user_groups[user] = [group]
            # Now add the group to the list of
# groups for this user, creating the entry
# in the dictionary if necessary

    return(user_groups)
